#**Huffman Coding Compression and Decompression Tool**

**Description:**
This project implements the Huffman coding algorithm for text compression and decompression. Huffman coding is a widely used algorithm for lossless data compression, especially for text files. The project provides a Django web application interface to upload a text file, compress it using Huffman coding, and download the compressed and decompressed files.

**Folder Structure:**
- **huffman_project/**: Django project directory containing the settings and configuration files.
  - **huffman_app/**: Django app directory containing the application logic.
    - **templates/**: HTML templates for the web interface.
    - **views.py**: Contains the Django views for handling file uploads, compression, and decompression.
    - **huffman.py**: Contains the Huffman coding algorithm implementation.
- **media/**: Directory to store uploaded files.
- **compressed_files/**: Directory to store compressed files.
- **decompressed_files/**: Directory to store decompressed files.

**How to Use:**
1. Clone the repository to your local machine.
2. Install Django if not already installed: `pip install Django`.
3. Navigate to the project directory: `cd huffman_project`.
4. Run the Django development server: `python manage.py runserver`.
5. Access the web application at `http://localhost:8000`.
6. Upload a text file using the provided form.
7. Click the "Upload and Compress" button to compress the file.
8. Once compressed, click the "Download Compressed File" button to download the compressed file.
9. To decompress the file, click the "Decompress" button, and then click the "Download Decompressed File" button to download the decompressed file.

**Note:** Ensure that you have the necessary permissions to write files to the `media/`, `compressed_files/`, and `decompressed_files/` directories.

**Additional Features:**
- Client-side validation to ensure a file is selected before uploading.
- Bootstrap styling for a clean and user-friendly interface.
- Error handling for cases where the file is not selected or the upload fails.

**Requirements:**
- Python (3.x recommended)
- Django
- Bootstrap (included via CDN)

**License:**
This project is licensed under the MIT License. See the LICENSE file for details.

**Author:**
[Your Name]

**Contributing:**
Feel free to contribute to this project by submitting pull requests or reporting issues on GitHub.
