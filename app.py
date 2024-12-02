from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from PIL import Image
import numpy as np

app = Flask(__name__)

# Increase maximum file size to 16MB
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load the Doctr OCR model once at startup
model = ocr_predictor(pretrained=True)

def post_process_text(text):
    if text:
        return text.strip()
    return ""

@app.route('/ocr', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            # Check if the POST request has the file part
            if 'file' not in request.files:
                return jsonify({'error': 'No file part'}), 400

            file = request.files['file']
            # If the user does not select a file, browser submits empty part
            if file.filename == '':
                return jsonify({'error': 'No selected file'}), 400
                
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
                    
                    # Return JSON response with formatted text
                    return jsonify({
                        'text': text,
                        'lines': text.split('\n')  # Add lines array for better formatting
                    }), 200
                    
                except Exception as e:
                    # Clean up file if processing fails
                    if os.path.exists(filepath):
                        os.remove(filepath)
                    return jsonify({'error': str(e)}), 500
                    
        except Exception as e:
            return jsonify({'error': str(e)}), 500
            
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
    ocr_texts = []
    
    for page in result.pages:
        for block in page.blocks:  # Changed from block.lines to page.blocks
            for line in block.lines:
                # Get all words in the line
                line_words = [word.value for word in line.words]
                # Join words with single space
                line_text = " ".join(line_words)
                # Clean up the text
                processed_text = post_process_text(line_text)
                if processed_text:  # Only add non-empty lines
                    ocr_texts.append(processed_text)

    # Join all lines with newline character
    return "\n".join(ocr_texts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5002", debug=False, threaded=True)
