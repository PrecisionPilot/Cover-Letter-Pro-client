from openai import OpenAI
from API_key import key

client = OpenAI(api_key=key)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "You are a helpful assistant."}],
    max_tokens=100,
)
for chunk in stream:
    print(chunk)