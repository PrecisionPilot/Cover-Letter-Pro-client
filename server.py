from flask import Flask, jsonify, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def main():
    app.logger.debug("Main page requested")
    return f"<p>Hello world</p>"

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("/var/www/uploads/uploaded_file.txt")

with app.test_request_context():
    pass

if __name__ == "__main__":
    app.run(debug=False, port=8080)