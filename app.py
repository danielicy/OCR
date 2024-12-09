from flask import Flask, request, render_template
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

app = Flask(__name__)

# Configure the path to the Tesseract-OCR installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file():
    return '''
    <h1>PDF OCR App</h1>
    <form action="/process" method="post" enctype="multipart/form-data">
        <input type="file" name="pdf" accept="application/pdf" required />
        <button type="submit">Upload and Process</button>
    </form>
    '''

@app.route('/process', methods=['POST'])
def process_file():
    if 'pdf' not in request.files:
        return "No file uploaded", 400

    file = request.files['pdf']
    if file.filename == '':
        return "No file selected", 400

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    try:
        # Convert PDF to images
        images = convert_from_path(file_path)

        # Perform OCR on each page
        ocr_text = ""
        for page_number, image in enumerate(images, start=1):
            text = pytesseract.image_to_string(image, lang='eng')
            ocr_text += f"\n--- Page {page_number} ---\n{text}\n"

        # Cleanup uploaded file
        os.remove(file_path)

        return f"<pre>{ocr_text}</pre>"

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
