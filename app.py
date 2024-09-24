from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder where uploaded files will be stored
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hashmatic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Allowed file extensions for image and video files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}

# Function to check if file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define a database model for the uploaded files
class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)

    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads
@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Save file metadata to the database
        uploaded_file = UploadedFile(filename=filename, filepath=filepath)
        db.session.add(uploaded_file)
        db.session.commit()

        return jsonify({"status": "success", "message": "File uploaded successfully!", "file_path": filepath})
    
    return jsonify({"status": "error", "message": "File type not allowed"})

# Route to view all uploaded files
@app.route('/uploads')
def view_uploads():
    files = UploadedFile.query.all()
    file_list = [{"id": file.id, "filename": file.filename, "filepath": file.filepath} for file in files]
    return jsonify(file_list)

if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Create the database tables
    db.create_all()
    
    app.run(debug=True)
