import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model = "gpt-4"

client = AzureOpenAI(api_key=api_key, api_version="2023-03-15-preview", azure_endpoint=endpoint)

def prompt(value):
    conversation = [{"role": "user", "content": value}, {"role": "system", "content": "NO fucking wayyy"}]
    response = client.chat.completions.create(model=model, messages=conversation)
    return response.choices[0].message.content

while(True):
    value = str(input("Enter Query: "))
    print((prompt(value)))