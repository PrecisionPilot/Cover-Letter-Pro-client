from openai import OpenAI
from API_key import key
from pdfquery import PDFQuery

def read_pdf(file) -> str:
    pdf = PDFQuery(file)
    pdf.load()
    text = [line.text for line in pdf.pq('LTTextLineHorizontal')]
    # Remove empty strings
    text = [line for line in text if line]
    return "\n".join(text)
text = read_pdf("server/resume.pdf")

client = OpenAI(api_key=key)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": f"Write a cover letter based on my experience: {text}"}],
    max_tokens=750,
)
print(stream.choices[0].message.content)