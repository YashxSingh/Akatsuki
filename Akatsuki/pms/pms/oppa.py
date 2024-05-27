import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model = "gpt-4"
username = input('Enter employee name : ')

client = AzureOpenAI(api_key=api_key, api_version="2023-03-15-preview", azure_endpoint=endpoint)

def gen_feedback(value, x):
    conversation = [{"role": "user", "content": value}, {"role": "system", "content": f"Give 50 words feedback in third person about {username}, a few keywords about whom are : {x}"}]
    response = client.chat.completions.create(model=model, messages=conversation)
    return response.choices[0].message.content

# while(True):
#     value = str(input("You: "))
#     if value.lower() == 'exit' or value.lower() == 'quit':
#         print('Have a nice day!! ')
#         break
#     print('\nGPT4: ', (prompt(value)), '\n')