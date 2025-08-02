# import os
import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Pencil Sketch App 🖌️")
st.write("Upload an image to convert it into a pencil sketch.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Convert to BGR (OpenCV uses BGR)
    if img_array.shape[2] == 4:  # RGBA
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2BGR)
    else:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = 255 - gray_image

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = 255 - blurred

    # Create the pencil sketch
    sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Show original and sketch
    st.subheader("Original Image")
    st.image(image, use_container_width = True)

    st.subheader("Pencil Sketch")
    st.image(sketch, use_container_width=True, channels="GRAY")






