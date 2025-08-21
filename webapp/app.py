import os
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
from werkzeug.utils import secure_filename

# GCS Config
BUCKET_NAME = "testpocnew1"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "storae.json"

app = Flask(__name__)

# Initialize GCS client
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

@app.route('/')
def index():
    blobs = bucket.list_blobs()
    files = [blob.name for blob in blobs]
    return render_template("index.html", files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    blob = bucket.blob(filename)
    blob.upload_from_file(file)

    return redirect(url_for("index"))

@app.route('/view/<filename>')
def view_file(filename):
    blob = bucket.blob(filename)
    url = blob.generate_signed_url(
        version="v4",
        expiration=3600,  # 1 hour
        method="GET",
        response_disposition="inline"  # 👉 ensures browser opens instead of downloading
    )
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
