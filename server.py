from flask import Flask, jsonify, request, url_for
from flask_cors import CORS
from markupsafe import escape
from openai import OpenAI
from API_key import key
import os
from pdfquery import PDFQuery

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=key)

def read_pdf(file) -> str:
    pdf = PDFQuery(file)
    pdf.load()
    text = [line.text for line in pdf.pq('LTTextLineHorizontal')]
    # Remove empty strings
    text = [line for line in text if line]
    return "\n".join(text)


@app.route("/api/receive_form", methods=['POST'])
def receive_form():
    files = request.files.to_dict()

    for file_key in files:
        file = files[file_key]
        if file.filename == '':
            return {'message': 'No selected file.'}, 400

        file.save("server/resume.pdf")

    resume = read_pdf("server/resume.pdf")
    # data = request.get_json()
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"Write a cover letter based on the following resume: {resume}"}],
        max_tokens=2000,
    )
    return {
        'message': stream.choices[0].message.content,
    }


with app.test_request_context():
    pass

if __name__ == "__main__":
    app.run(debug=False, port=8080)