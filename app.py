from flask import Flask, request, render_template, redirect, url_for
import os
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from PIL import Image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
# Increase maximum file size to 16MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load the Doctr OCR model once at startup
model = ocr_predictor(pretrained=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            # Check if the POST request has the file part
            if 'file' not in request.files:
                return {'error': 'No file part'}, 400
            
            file = request.files['file']
            # If the user does not select a file, browser submits empty part
            if file.filename == '':
                return {'error': 'No selected file'}, 400
                
            if file:
                # Save the uploaded file
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                try:
                    # Process the file with OCR
                    text = process_file(filepath)
                    # Remove the file after processing
                    os.remove(filepath)
                    
                    # Return JSON response
                    return {'text': text}, 200
                    
                except Exception as e:
                    # Clean up file if processing fails
                    if os.path.exists(filepath):
                        os.remove(filepath)
                    return {'error': str(e)}, 500
                    
        except Exception as e:
            return {'error': str(e)}, 500
            
    # GET request - return simple HTML form
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
    # Run with increased timeout
    app.run(host='0.0.0.0', debug=False, threaded=True)