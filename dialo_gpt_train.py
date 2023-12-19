import numpy as np
from datasets import load_dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TrainingArguments, Trainer
import os
from config import CHAT_ENGINE_MODEL_OUTPUT
import time
from datetime import timedelta

start = time.time()

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# Load the DailyDialog dataset
dataset = load_dataset('csebuetnlp/dailydialogue_bn')


# Concatenate all utterances within a dialogue and map to 'dialog' key
def concatenate_utterances(example):
    example['dialogue'] = " ".join(example['dialogue'])
    return example


# Apply the function to all examples in the dataset
dataset = dataset.map(concatenate_utterances)

print(dataset["train"][:1])
print(dataset["validation"][:1])
print(dataset["test"][:1])
# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(CHAT_ENGINE_MODEL_OUTPUT)
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained(CHAT_ENGINE_MODEL_OUTPUT)


# Encode the dataset
def encode(examples):
    encoded = tokenizer(examples['dialogue'], truncation=True, padding='max_length', max_length=128)
    encoded['labels'] = encoded['input_ids'][:]
    return encoded


encoded_dataset = dataset.map(encode, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir=CHAT_ENGINE_MODEL_OUTPUT,   # output directory
    num_train_epochs=100,             # total number of training epochs
    per_device_train_batch_size=8,  # batch size per device during training
    per_device_eval_batch_size=16,   # batch size for evaluation
    warmup_steps=500,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    logging_dir=None,                # directory for storing logs
    save_total_limit=1,
    save_strategy="no",
    fp16=True                        # use floating point 16 bit precision for training
)

# Create Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset['train'],
    eval_dataset=encoded_dataset['validation']
)

# Evaluate before fine-tuning
pre_eval_results = trainer.evaluate(encoded_dataset['validation'])

# Get predictions for validation set before fine tuning for 10 samples
pre_val_predictions = trainer.predict(encoded_dataset['validation'].select(range(10)))

print("training...")
try:
    trainer.train()
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    pass

tokenizer.save_pretrained(CHAT_ENGINE_MODEL_OUTPUT)
trainer.save_model()
print(f"Saved in {CHAT_ENGINE_MODEL_OUTPUT}")

# Get predictions for validation set before fine tuning for 10 samples
pre_val_predictions = trainer.predict(encoded_dataset['validation'].select(range(10)))
# Evaluate after fine-tuning
post_eval_results = trainer.evaluate(encoded_dataset['validation'])

# Print the evaluation losses before and after fine-tuning
print('Evaluation Results before fine-tuning :', pre_eval_results['eval_loss'])
print('Evaluation Results after fine-tuning  :', post_eval_results['eval_loss'])

# Get predictions for validation set before fine tuning for 10 samples
post_val_predictions = trainer.predict(encoded_dataset['validation'].select(range(10)))

# Zip the pre and post tuning predictions
predictions = zip(pre_val_predictions.predictions, post_val_predictions.predictions)

for idx, (pre, post) in enumerate(predictions):
    pre_pred = tokenizer.decode(np.argmax(pre, axis=-1), skip_special_tokens=True)
    post_pred = tokenizer.decode(np.argmax(post, axis=-1), skip_special_tokens=True)
    ground_truth = encoded_dataset['validation'][idx]["dialogue"]

    print('Ground truth \n' + ground_truth + '\n')
    print('Pre-prediction \n' + pre_pred + '\n')
    print('Post-prediction \n' + post_pred + '\n')
    print('-------------------' * 4, end='\n')


print("time taken {}".format(timedelta(seconds=time.time() - start)))
