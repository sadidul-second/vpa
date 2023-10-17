from transformers import AutoTokenizer, GPTNeoForQuestionAnswering
import torch

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = GPTNeoForQuestionAnswering.from_pretrained("EleutherAI/gpt-neo-1.3B")

question, text = "what is your name?", "Your name is Mariah, you are a helpful personal assistant."

inputs = tokenizer(question, text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

answer_start_index = outputs.start_logits.argmax()
answer_end_index = outputs.end_logits.argmax()
print(answer_end_index)

predict_answer_tokens = inputs.input_ids[0, answer_start_index: answer_end_index + 1]

# target is "nice puppet"
target_start_index = torch.tensor([0])
target_end_index = torch.tensor([15])
#
outputs = model(**inputs, start_positions=target_start_index, end_positions=target_end_index)
loss = outputs.loss
answer_start_index = outputs.start_logits.argmax()
answer_end_index = outputs.end_logits.argmax()
predict_answer_tokens = inputs.input_ids[0, answer_start_index: answer_end_index + 1]
gen_text = tokenizer.batch_decode(predict_answer_tokens)
print(outputs)
print(gen_text)


