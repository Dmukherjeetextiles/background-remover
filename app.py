import streamlit as st
from PIL import Image
from rembg import remove
import io
import base64

def upload_single_image():
    """Function to upload a single image."""
    st.subheader("Single Mode")
    st.write("Upload an image and remove the background :wink:")

    # Upload a single image
    uploaded_file = st.file_uploader("Choose your image...", accept_multiple_files=False, type=["jpg", "jpeg", "png"])

    return uploaded_file

def upload_multiple_images():
    """Function to upload multiple images."""
    st.subheader("Xtreme Mode")
    st.write("Upload multiple images and remove all of their backgrounds with one click :sunglasses:")

    # Upload multiple images
    multi_uploaded_files = st.file_uploader("Choose your images...", accept_multiple_files=True, type=["jpg", "jpeg", "png"], key="multi_mode")

    return multi_uploaded_files

def process_and_display_single_image(image):
    """Process uploaded image, remove background, and display refined image."""
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Run"):
        # Process image with rembg (local processing)
        refined_image = remove(image)

        # Display the refined image
        st.image(refined_image, caption='Refined Image', use_column_width=True)

        # Download button (maintaining transparency)
        buffered = io.BytesIO()
        refined_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        href = f'<a href="data:file/png;base64,{img_str}" download="refined_image.png">Download Image</a>'
        st.markdown(href, unsafe_allow_html=True)

def process_and_display_multiple_images(multi_uploaded_files):
    """Process uploaded images, remove backgrounds, and display refined images."""
    if st.button("Run"):
        for file_idx, file in enumerate(multi_uploaded_files):
            image = Image.open(file)
            refined_image = remove(image)

            # Display the refined image
            st.image(refined_image, caption=f'Refined Image {file_idx + 1}', use_column_width=True)

            # Download (maintaining transparency)
            buffered = io.BytesIO()
            refined_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            href = f'<a href="data:file/png;base64,{img_str}" download="refined_image_{file_idx + 1}.png">Download Image {file_idx + 1}</a>'
            st.markdown(href, unsafe_allow_html=True)

def main():
    st.title("One-Click Background Removing")

    # Sidebar options
    mode = st.sidebar.radio("Select Mode", ("Single Mode", "Xtreme Mode"))

    if mode == "Single Mode":
        # Upload a single image
        uploaded_file = upload_single_image()

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            process_and_display_single_image(image)
    else:
        # Upload multiple images
        multi_uploaded_files = upload_multiple_images()

        if multi_uploaded_files:
            process_and_display_multiple_images(multi_uploaded_files)

if __name__ == "__main__":
    main()
