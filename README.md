# Advanced OCR Flask App

This Flask application provides an advanced Optical Character Recognition (OCR) service using the Doctr library. It allows users to upload images or PDF files and extract text content from them.

## Features

- Web interface for file uploads
- Supports both image and PDF file formats
- Uses Doctr OCR model for accurate text extraction
- Displays extracted text in a user-friendly format

## Prerequisites

- Python 3.7+
- Flask
- Doctr
- Pillow
- NumPy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Advanced-OCR-Flask-App.git
   cd Advanced-OCR-Flask-App
   ```

2. Install the required dependencies:
   ```
   pip install flask doctr pillow numpy
   ```

3. Create an `uploads` folder in the project directory:
   ```
   mkdir uploads
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Upload an image or PDF file using the web interface

4. View the extracted text on the results page

## Project Structure

- `app.py`: Main Flask application file
- `templates/`:
  - `upload.html`: HTML template for the file upload page
  - `result.html`: HTML template for displaying OCR results
- `uploads/`: Temporary storage for uploaded files (automatically created)

## How It Works

1. The user uploads a file through the web interface
2. The file is temporarily saved in the `uploads` folder
3. The OCR model processes the file and extracts text
4. The extracted text is displayed to the user
5. The uploaded file is removed from the server

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

