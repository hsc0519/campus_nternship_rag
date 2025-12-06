# llm.py
from openai import AzureOpenAI

with open("api_key.txt", 'r') as file:
    api_key = file.read().strip()

endpoint = "https://20250408-genai-group-1.openai.azure.com/"
deployment = "genai-gpt-4o"
api_version = "2025-01-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

def chat_response(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.5,
        model=deployment
    )
    return response.choices[0].message.content.strip()
