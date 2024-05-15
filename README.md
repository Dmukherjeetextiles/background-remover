# One-Click Background Removing
This Python application offers a user-friendly way to remove the background from images in a single click.
## Functionality:
- Select Mode: "Single" for a single image and "Xtreme" for multiple images
- Image Upload: Upload your image (JPG, JPEG, or PNG format) for processing.
- Background Removal: With a simple button click, remove the background from the uploaded image.
- Transparency Preservation: The processed image maintains its transparency, ensuring seamless integration into various projects.
- Download Option: Download the background-removed image as a PNG file for further use.
- Download All: Download multiple images in a zip file(only available in "Xtreme")
## Dependencies:
To run this application, Click [here](https://background-removing.streamlit.app/)

## Local Installation:
- Clone the Repository:
`git clone https://github.com/Dmukherjeetextiles/background-remover.git`
- Install Dependencies:
`pip install streamlit Pillow rembg`
- Running the App:
## Navigate to the project directory in your terminal.
Execute the following command:
`streamlit run app.py`
This will launch the application in your web browser.
## Usage:
- Select mode(Default mode: Single)
- Use the file uploader to select your desired image.
- Click the "Run" button to initiate the background removal process.
- The processed image with the removed background will be displayed.
- Click the "Download Image" link or "Download All Images" link(for Xtreme mode) to save the result(s) in PNG format.
## Additional Notes:
The rembg library leverages Stable Diffusion XL refiner for background removal, which means the accuracy may vary depending on the image's content and complexity.
The application is designed to preserve transparency in the output image, making it ideal for images with high-contrast backgrounds.
## Credits:
[Rembg Library](https://github.com/danielgatis/rembg)

[Streamlit](https://streamlit.io/)

[Pillow](https://pillow.readthedocs.io/)
