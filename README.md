# Background Removal Streamlit App with Rembg
This Streamlit application offers a user-friendly way to remove the background from images using the rembg library.
## Functionality:
- Image Upload: Upload your image (JPG, JPEG, or PNG format) for processing.
- Background Removal: With a simple button click, remove the background from the uploaded image.
- Transparency Preservation: The processed image maintains its transparency, ensuring seamless integration into various projects.
- Download Option: Download the background-removed image as a PNG file for further use.
## Dependencies:
To run this application, you'll need the following Python libraries:
- streamlit
- Pillow
- rembg
## Installation:
- Clone the Repository:
`git clone https://github.com/Dmukherjeetextiles/background-remover.git`
- Install Dependencies:
`pip install streamlit Pillow rembg`
- Running the App:
## Navigate to the project directory in your terminal.
Execute the following command:
`streamlit run app.py`
This will launch the application in your web browser. Here is my deployed [link](https://background-removing.streamlit.app/).
## Usage:
- Use the file uploader to select your desired image.
- Click the "Remove Background" button to initiate the background removal process.
- The processed image with the removed background will be displayed.
- Click the "Download Image" button to save the result as a PNG file.
## Additional Notes:
The rembg library leverages machine learning models for background removal, which means the accuracy may vary depending on the image's content and complexity.
The application is designed to preserve transparency in the output image, making it ideal for images with transparent backgrounds.
## Credits:
[Rembg Library: ](https://github.com/danielgatis/rembg)
[Streamlit: ](https://streamlit.io/)
[Pillow: ](https://pillow.readthedocs.io/)
