import streamlit as st
from PIL import Image
from main import extract_palette, create_color_palette
import io

st.set_page_config(page_title="imagRGB", layout="centered")
st.title("imagRGB")
st.write("A simple tool to extract color palettes from images")
uploaded_file = st.file_uploader("Upload JPEG Image", type=["jpeg", "jpg", "png", "tif", "tiff", "bmp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')

    num_colors = st.slider('Number of Colors', 2, 10, 5)
    percentile = st.slider('Percentile', 1, 100, 15)
    st.markdown("""
    <style>
    .help-text {
        display: inline;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 300px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position the tooltip above the text */
        left: 50%;
        margin-left: -150px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
    <p class="help-text">Lower percentile values tend to be darker and have more contrast.</p>
    <div class="tooltip">ℹ️
        <span class="tooltiptext">The percentile property determines the specific percentile value used to calculate the color centroids from the clusters identified by the K-Means algorithm. This helps in refining the color extraction process by focusing on a specific percentile of the color distribution within each cluster, allowing for more accurate and representative color palettes.</span>
    </div>
    <br/><br/>
    """, unsafe_allow_html=True)

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