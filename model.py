import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"} 

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error {response.status_code}: {response.json().get('error', 'Unknown error')}")
        return None


st.title("Text-to-Image Generator")
st.write("Enter a description below, and the model will generate an image based on it.")


text_input = st.text_input("Enter a description:", "Astronaut riding a horse")

if st.button("Generate Image"):
    if text_input:
        st.write("Generating image...")
        image_bytes = query({"inputs": text_input})

        # Display the generated image if successful
        if image_bytes:
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a description to generate an image.")


