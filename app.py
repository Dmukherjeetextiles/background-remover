import streamlit as st
from PIL import Image
from rembg import remove
import io
import base64

def main():
    """Main function of the Streamlit app."""
    st.title("One-Click Background Removal")
    st.subheader("Single Mode:")
    st.write("Upload your JPG/JPEG/PNG image, click the remove background button, and download the refined image.")

    # Upload single image
    single_uploaded_file = st.file_uploader("Choose one image...", type=["jpg", "jpeg", "png"], key="single_mode")

    if single_uploaded_file is not None:
        process_and_display(single_uploaded_file)

    st.subheader("Multi-Mode:")
    st.write("Upload multiple JPG/JPEG/PNG images (up to 15 files, total size less than 200 MB), and remove backgrounds with one click.")

    # Upload multiple images
    multi_uploaded_files = st.file_uploader("Choose multiple images...", accept_multiple_files=True, type=["jpg", "jpeg", "png"], key="multi_mode")

    if multi_uploaded_files:
        if len(multi_uploaded_files) > 15:
            st.error("You can upload a maximum of 15 files.")
        else:
            total_size = sum(f.size for f in multi_uploaded_files)
            if total_size > 200*1024*1024:
                st.error("Total size of uploaded files exceeds 200 MB.")
            else:
                if st.button("Remove Background (Multi-Mode)"):
                    for file_idx, file in enumerate(multi_uploaded_files):
                        st.write(f"Image {file_idx + 1}:")
                        process_and_display(file, identifier=file_idx)

def process_and_display(uploaded_file, identifier=None):
    """Process uploaded image, remove background, and display refined image."""
    image = Image.open(uploaded_file)
    st.image(image, caption=f'Uploaded Image {identifier + 1}', use_column_width=True)

    if st.button("Remove Background"):
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

if __name__ == "__main__":
    main()
