from PIL import Image, ImageDraw, ImageFont
from sklearn.cluster import KMeans
import numpy as np
import os

def extract_colors(image_path, num_colors):
    image = Image.open(image_path)
    image = image.resize((150, 150))
    image_array = np.array(image)
    pixels = image_array.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_
    colors = colors.round().astype(int)
    
    return colors

def create_color_palette(colors, output_path):
    color_height = 200
    width, height = 800, color_height * len(colors)
    palette = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(palette)
    font_size = 24
    
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

    for i, color in enumerate(colors):
        top = i * color_height
        draw.rectangle([0, top, width, top + color_height], fill=tuple(color))
        
        rgb_text = f"RGB({color[0]}, {color[1]}, {color[2]})"
        hex_text = f"HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}".upper()
        cmyk_text = f"CMYK: {color[0]/255:.2f}, {color[1]/255:.2f}, {color[2]/255:.2f}"
        text_list = [rgb_text, hex_text, cmyk_text]

        text_top = 10
        text_spacing = 30
        for j, text in enumerate(text_list):
            draw.text((20, top + text_top + j * text_spacing), text, fill='black' if sum(color) > 382 else 'white', font=font)

    palette.save(output_path, dpi=(300, 300))
    print(f"Color palette saved to {output_path}")

def main():
    IMAGE_PATH = "example-images/fog-mountain-green-landscape.jpg"
    NUM_COLORS = 4
    OUTPUT_DIR = "./palletes/"

    file_name = IMAGE_PATH.split("/")[-1].split(".")[0]
    colors = extract_colors(IMAGE_PATH, NUM_COLORS)
    
    os.makedirs(os.path.dirname(OUTPUT_DIR), exist_ok=True)

    create_color_palette(colors, f"{OUTPUT_DIR}{file_name}-palette.png")

if __name__ == "__main__":
    main()