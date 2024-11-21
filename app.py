import streamlit as st
from PIL import Image
from main import extract_palette, create_color_palette
import io

st.set_page_config(page_title="imagRGB", layout="centered")
st.title("imagRGB")
st.write("A simple tool to extract color palettes from images")
uploaded_file = st.file_uploader("Upload JPEG Image", type=["jpeg", "jpg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')

    num_colors = st.slider('Number of Colors', 2, 10, 5)
    percentile = st.slider('Percentile', 1, 100, 15)

    colors = extract_palette(image, num_colors, percentile)
    palette = create_color_palette(colors)
    
    st.image(palette, caption='Generated Color Palette')

    buf = io.BytesIO()
    palette.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Color Palette",
        data=byte_im,
        file_name="color_palette.png",
        mime="image/png"
    )