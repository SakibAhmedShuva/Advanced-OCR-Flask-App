# Advanced OCR Flask App (Image / PDF)

This Flask application provides an advanced Optical Character Recognition (OCR) service using the Doctr library. It allows users to upload images or PDF files and extract text content from them, with support for both local deployment and containerized environments using Docker.

## Features

- Web interface for file uploads
- Supports both image and PDF file formats
- Uses Doctr OCR model for accurate text extraction
- Displays extracted text in a user-friendly format
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

## Installation

### Local Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Advanced-OCR-Flask-App.git
   cd Advanced-OCR-Flask-App
   ```

2. Install the required dependencies:
   ```bash
   pip install flask doctr pillow numpy
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

The application will be available at `http://localhost:5000`.

## Usage

1. Start the application:
   - Local: `python app.py`
   - Docker: `docker-compose up`

2. Open a web browser and navigate to `http://localhost:5000`

3. Upload an image or PDF file using the web interface

4. View the extracted text on the results page

## Project Structure

```
.
├── app.py                 # Main Flask application file
├── Dockerfile            # Docker configuration file
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── templates/
│   ├── upload.html      # HTML template for file upload page
│   └── result.html      # HTML template for displaying OCR results
├── uploads/             # Temporary storage for uploaded files
└── README.md            # Project documentation
```

## Technical Details

### Docker Configuration
- Base image: Python 3.10.11-slim
- Memory limits: 2GB maximum, 1GB reserved
- Exposed port: 5000
- Mounted volumes for models and sessions
- Automatic container restart policy
- Environment variables configured for production

### Application Features
- Threaded execution for better performance
- Automatic file cleanup after processing
- Error handling for file uploads and processing
- Support for both PDF and image formats
- Memory-efficient processing

## Security Considerations

- File size limited to 16MB
- Temporary file storage with automatic cleanup
- Containerized environment for isolation
- Input validation for file uploads
- Error handling and logging

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
   - Check file size limits
   - Verify supported file formats
   - Ensure uploads directory permissions

3. **OCR Quality Issues**
   - Verify input image quality
   - Check supported languages and formats
   - Review model configuration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
