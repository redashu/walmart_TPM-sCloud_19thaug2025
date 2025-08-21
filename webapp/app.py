from flask import Flask, request, render_template, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__)

# GCS Config
BUCKET_NAME = "testpocnew1"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "storae.json"

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

@app.route('/')
def index():
    # List all files in GCS bucket
    blobs = bucket.list_blobs()
    files = [blob.name for blob in blobs]
    return render_template("index.html", files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    blob = bucket.blob(file.filename)
    blob.upload_from_file(file, content_type=file.content_type)

    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download(filename):
    blob = bucket.blob(filename)
    return blob.download_as_bytes()

if __name__ == "__main__":
    app.run(debug=True)
