import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model = "gpt-4"

client = AzureOpenAI(api_key=api_key, api_version="2023-03-15-preview", azure_endpoint=endpoint)

def gen_feedback(emp_name, qual):
    conversation = [{"role": "user", "content": "Give the response in simple english."}, {"role": "system", "content": f"Give 100 words feedback about {emp_name}, addressing the feedback to him. Some keywords about what to inculde in feedback are : {qual}"}]
    response = client.chat.completions.create(model=model, messages=conversation)
    return response.choices[0].message.content