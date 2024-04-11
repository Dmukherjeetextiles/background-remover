import streamlit as st
from PIL import Image
import requests
import io

# Define the Hugging Face API URL for the u2net model
API_URL = "https://api-inference.huggingface.co/models/u2net/u2net"


def process_image(image_data, api_key):
    """Processes an image by removing the background using the u2net API."""
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(API_URL, headers=headers, files={"image": image_data})

    if response.status_code == 200:
        mask_data = response.content
        mask_image = Image.open(io.BytesIO(mask_data)).convert("L")  # Convert to grayscale

        # Apply mask to the original image to remove background
        original_image = Image.open(io.BytesIO(image_data)).convert("RGBA")
        empty_image = Image.new("RGBA", original_image.size, 0)
        refined_image = Image.composite(original_image, empty_image, mask_image)
        return refined_image
    else:
        st.write(f"Error: {response.status_code}, {response.text}")
        return None


def main():
    """Main function of the Streamlit app."""
    st.title("Background Removal with U2Net")

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
