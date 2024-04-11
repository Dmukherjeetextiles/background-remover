import streamlit as st
from PIL import Image
import requests
import io

# Define the Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-refiner-1.0"


def process_image(image_data, api_key):
    """Processes an image by removing the background using the API."""
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(API_URL, headers=headers, data=image_data)
    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content))
    else:
        st.write(f"Error: {response.status_code}, {response.text}")
        return None


def main():
    """Main function of the Streamlit app."""
    st.title("Background Removal with Stable Diffusion XL Refiner")

    # Get API key from secrets
    api_key = st.secrets["API_KEY"]

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Process image and get refined image
        refined_image = process_image(uploaded_file.getvalue(), api_key)

        if refined_image is not None:
            # Display the refined image
            st.image(refined_image, caption='Refined Image', use_column_width=True)

            # Download button
            btn = st.download_button(
                label="Download Image",
                data=refined_image,
                file_name="refined_image.png",
                mime="image/png"
            )


if __name__ == "__main__":
    main()
