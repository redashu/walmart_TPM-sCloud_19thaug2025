from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__)

# GCS Config
BUCKET_NAME = "testpocnew1"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "storae.json"

storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

@app.route("/")
def index():
    blobs = bucket.list_blobs()
    files = [blob.name for blob in blobs]
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        blob = bucket.blob(file.filename)
        # ✅ Set correct content type
        blob.upload_from_file(file, content_type=file.content_type)
    return redirect(url_for("index"))

@app.route("/view/<filename>")
def view_file(filename):
    blob = bucket.blob(filename)
    url = blob.generate_signed_url(version="v4", expiration=3600, method="GET")
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
