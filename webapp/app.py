from flask import Flask, request, render_template, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__)

# GCS Config
BUCKET_NAME = "testpocnew1"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "storae.json"

# Initialize GCS client
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

@app.route("/")
def index():
    """List all files in the GCS bucket"""
    blobs = bucket.list_blobs()
    files = [blob.name for blob in blobs]
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload_file():
    """Upload a file to GCS"""
    if "file" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    return redirect(url_for("index"))

@app.route("/view/<filename>")
def view_file(filename):
    """Generate a public URL for file"""
    blob = bucket.blob(filename)
    url = blob.generate_signed_url(version="v4", expiration=3600, method="GET")
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
