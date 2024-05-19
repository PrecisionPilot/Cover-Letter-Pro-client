from openai import OpenAI
from API_key import key

client = OpenAI(api_key=key)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "Write a cover letter based on my experience"}],
    max_tokens=500,
)
print(stream.choices[0].message.content)