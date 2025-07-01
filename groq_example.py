# Example using Groq API (OpenAI-compatible)
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('api.env')

client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),  # Add this to your api.env
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama3-8b-8192",  # or "mixtral-8x7b-32768"
    messages=[
        {"role": "user", "content": "Explain AI to a 5-year-old"}
    ]
)

print(response.choices[0].message.content)