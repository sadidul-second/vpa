# from transformers import pipeline, Conversation
# converse = pipeline("conversational", model="microsoft/DialoGPT-medium", framework="pt")
#
# conversation_1 = Conversation("Going to the movies tonight - any suggestions?")
# conversation_2 = Conversation("What's the last book you have read?")
# result = converse([conversation_1, conversation_2])
# print(result)
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Let's chat for 5 lines
for step in range(5):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')
    print("user input", new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    try:
        print("hist 1", chat_history_ids)
    except NameError:
        pass

    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    try:
        print("hist 2", chat_history_ids)
    except NameError:
        pass
    # pretty print last ouput tokens from bot
    print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
