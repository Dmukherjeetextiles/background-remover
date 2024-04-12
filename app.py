import streamlit as st
from PIL import Image
from rembg import remove

def main():
    """Main function of the Streamlit app."""
    st.title("Background Removal with Rembg")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Remove Background"):
            # Process image with rembg (local processing)
            refined_image = remove(image)

            # Display the refined image
            st.image(refined_image, caption='Refined Image', use_column_width=True)

            # Download button (maintaining transparency)
            btn = st.download_button(
                label="Download Image",
                data=refined_image,
                file_name="refined_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
