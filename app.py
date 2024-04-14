import streamlit as st
from PIL import Image
from rembg import remove
import io
import base64

def upload_images():
    """Function to upload multiple images."""
    st.subheader("Multi-Mode:")
    st.write("You may upload single or multiple JPG/JPEG/PNG images (up to 15 files), and remove backgrounds with one click.")

    # Upload multiple images
    multi_uploaded_files = st.file_uploader("Choose your images...", accept_multiple_files=True, type=["jpg", "jpeg", "png"], key="multi_mode")

    return multi_uploaded_files

def process_and_display_image(image, identifier=None):
    """Process uploaded image, remove background, and display refined image."""
    st.image(image, caption=f'Uploaded Image {identifier + 1}', use_column_width=True)

    if st.button(f"Remove Background {identifier + 1}"):
        # Process image with rembg (local processing)
        refined_image = remove(image)

        # Display the refined image
        st.image(refined_image, caption=f'Refined Image {identifier + 1}', use_column_width=True)

        # Download button (maintaining transparency)
        buffered = io.BytesIO()
        refined_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        href = f'<a href="data:file/png;base64,{img_str}" download="refined_image_{identifier}.png">Download Image</a>'
        st.markdown(href, unsafe_allow_html=True)

def main():
    """Main function of the Streamlit app."""
    st.title("One-Click Background Removal")

    # Upload images
    multi_uploaded_files = upload_images()

    if multi_uploaded_files:
        if len(multi_uploaded_files) > 15:
            st.error("You can upload a maximum of 15 files.")
        else:
            total_size = sum(f.size for f in multi_uploaded_files)
            if total_size > 200*1024*1024:
                st.error("Total size of uploaded files exceeds 200 MB.")
            else:
                if st.button("Multi-Mode Xtreme"):
                    for file_idx, file in enumerate(multi_uploaded_files):
                        st.write(f"Image {file_idx + 1}:")
                        image = Image.open(file)
                        process_and_display_image(image, identifier=file_idx)

if __name__ == "__main__":
    main()
