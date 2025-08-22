from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from google.cloud import storage
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL connection
db = mysql.connector.connect(
    host="34.131.212.48",
    user="root",
    password="your_db_password",  # replace with real
    database="appdb"
)
cursor = db.cursor(dictionary=True)

# Google Cloud Storage Config
GCS_BUCKET = "testpocnew1"  # replace with your bucket name
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "storae.json"  # service account json

storage_client = storage.Client()
bucket = storage_client.bucket(GCS_BUCKET)


@app.route("/")
def home():
    if "username" not in session:   # 👈 Protect homepage
        return redirect(url_for("login"))

    files = [blob.name for blob in bucket.list_blobs()]
    return render_template("index.html", files=files)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user:
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        if "file" not in request.files:
            flash("No file selected!", "danger")
            return redirect(url_for("upload"))

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected!", "danger")
            return redirect(url_for("upload"))

        blob = bucket.blob(file.filename)
        blob.upload_from_file(file, content_type=file.content_type)

        flash("File uploaded successfully to GCS!", "success")
        return redirect(url_for("home"))

    files = [blob.name for blob in bucket.list_blobs()]
    return render_template("index.html", files=files)

@app.route("/view/<filename>")
def view_file(filename):
    blob = bucket.blob(filename)
    url = blob.generate_signed_url(version="v4", expiration=3600)  # 1 hour signed URL
    return redirect(url)


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
