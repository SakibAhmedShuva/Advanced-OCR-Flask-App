# OCR Flask App
This Flask application provides an Optical Character Recognition (OCR) service using the Doctr library. It allows users to upload images or PDF files and extract text content from them, with support for both local deployment and containerized environments using Docker.

## Features
- Web interface for file uploads
- Supports both image and PDF file formats
- Uses Doctr OCR model for accurate text extraction
- Returns extracted text in JSON format
- Docker support for easy deployment and scalability
- Memory management and resource allocation
- File size limit of 16MB for uploads
- Automatic cleanup of processed files

## Prerequisites
### Local Installation
- Python 3.10.11
- Flask
- Doctr
- Pillow
- NumPy

### Docker Installation
- Docker
- Docker Compose

## Project Structure
```
.
├── app.py                 # Main Flask application file
├── Dockerfile            # Docker configuration file
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── templates/
│   └── upload.html      # HTML template for file upload page
└── uploads/             # Temporary storage for uploaded files
```

## Installation
### Local Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ocr-flask-app.git
   cd ocr-flask-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create an `uploads` folder in the project directory:
   ```bash
   mkdir uploads
   ```

### Docker Installation
1. Clone the repository as shown above
2. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```

The application will be available at `http://localhost:5002` (or the port specified in your app.py).

## Usage
1. Start the application:
   - Local: `python app.py`
   - Docker: `docker-compose up`
2. Open a web browser and navigate to `http://localhost:5002`
3. Upload an image or PDF file using the web interface
4. Receive the extracted text in JSON format

## Technical Details

### Docker Configuration
- Base image: Python 3.10.11-slim
- Memory limits: 2GB maximum, 1GB reserved
- Exposed port: 5000 (mapped from internal port 5002)
- Mounted volumes for models and sessions
- Automatic container restart policy
- Environment variables:
  - PYTHONUNBUFFERED=1
  - FLASK_APP=app.py
  - FLASK_ENV=production
  - USE_TORCH=1

### Application Features
- Threaded execution for better performance
- Automatic file cleanup after processing
- Error handling for file uploads and processing
- Support for both PDF and image formats
- Memory-efficient processing
- JSON response format with text and line-by-line results

## Security Considerations
- File size limited to 16MB
- Temporary file storage with automatic cleanup
- Containerized environment for isolation
- Input validation for file uploads
- Error handling and logging

## API Endpoints

### `/ocr`
- Methods: GET, POST
- GET: Returns the upload form HTML
- POST: Processes the uploaded file
  - Request: multipart/form-data with 'file' field
  - Response: JSON containing:
    - `text`: Full extracted text
    - `lines`: Array of text lines
  - Error Response: JSON with 'error' field

## Error Handling
The application handles several types of errors:
- No file uploaded
- Empty file selection
- File processing errors
- OCR processing errors

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes:
1. Fork the repository
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

## Troubleshooting

### Common Issues
1. **Container Memory Issues**
   - Adjust memory limits in docker-compose.yml
   - Monitor container resources using `docker stats`

2. **File Upload Errors**
   - Check file size limits (16MB maximum)
   - Verify supported file formats (images and PDFs)
   - Ensure uploads directory permissions are correct

3. **OCR Quality Issues**
   - Verify input image quality
   - Check PDF file compatibility
   - Ensure proper image format conversion

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
