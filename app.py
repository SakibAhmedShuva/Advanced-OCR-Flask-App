from flask import Flask, request, render_template, redirect, url_for
import os
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from PIL import Image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load the Doctr OCR model once at startup
model = ocr_predictor(pretrained=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser may submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            # Save the uploaded file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Process the file with OCR
            text = process_file(filepath)
            # Remove the file after processing
            os.remove(filepath)
            # Render a template to display the extracted text
            return render_template('result.html', text=text)
    else:
        # Display the upload form
        return render_template('upload.html')

def process_file(filepath):
    # Determine if the file is an image or PDF
    if filepath.lower().endswith('.pdf'):
        # Process PDF
        doc = DocumentFile.from_pdf(filepath)
        result = model(doc)
    else:
        # Process image
        image = Image.open(filepath).convert('RGB')
        image = np.array(image)
        result = model([image])
    # Extract text from the OCR result
    text_output = ""
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                line_text = " ".join([word.value for word in line.words])
                text_output += line_text + "\n"
    return text_output

if __name__ == '__main__':
    app.run(debug=True)
