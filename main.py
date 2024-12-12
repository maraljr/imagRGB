from PIL import Image, ImageDraw, ImageFont
import cv2
from sklearn.cluster import KMeans
import numpy as np
import os
import argparse

def extract_palette(image, n_colors, percentile):
    """
    Extracts a color palette from an image using K-Means clustering and percentile-based centroids.

    Args:
        image (PIL.Image.Image): The input image.
        n_colors (int): Number of colors to extract.
        percentile (int): Percentile for color extraction.

    Returns:
        np.ndarray: Array of extracted colors.
    """
    # Convert PIL image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    # Apply K-Means to get initial clusters
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image)
    labels = kmeans.labels_
    # Calculate the percentile-based centroids
    centroids = np.zeros((n_colors, 3))
    for i in range(n_colors):
        cluster_points = image[labels == i]
        centroids[i] = np.percentile(cluster_points, percentile, axis=0)
    return centroids.round().astype(int)

def create_color_palette(colors):
    """
    Creates an image of a color palette from a list of colors.

    Args:
        colors (np.ndarray): Array of colors.

    Returns:
        PIL.Image.Image: Image of the color palette.
    """
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

    return palette

def save_palette(palette, output_path):
    """
    Saves the color palette image to the specified path.

    Args:
        palette (PIL.Image.Image): The color palette image.
        output_path (str): Path to save the image.
    """
    palette.save(output_path, dpi=(300, 300))
    print(f"Color palette saved to {output_path}")

def check_range(value, min_val, max_val):
    """
    Checks if a value is within a specified range.

    Args:
        value (str): The value to check.
        min_val (int): Minimum allowed value.
        max_val (int): Maximum allowed value.

    Returns:
        int: The validated integer value.

    Raises:
        argparse.ArgumentTypeError: If the value is not within the range.
    """
    ivalue = int(value)
    if ivalue < min_val or ivalue > max_val:
        raise argparse.ArgumentTypeError(f"Value must be between {min_val} and {max_val}")
    return ivalue

def main():
    """
    Main function to generate a color palette from an image.
    """
    parser = argparse.ArgumentParser(description="Generate a color palette from an image.")
    parser.add_argument("image_path", type=str, help="Path to the input image file.")
    parser.add_argument("--num_colors", type=lambda x: check_range(x, 1, 10), default=5, help="Number of colors to extract from the image. 1-10. Default is 5.")
    parser.add_argument("--output_dir", type=str, default="./palettes/", help="Directory to save the color palette image. Default is ./palettes/")
    parser.add_argument("--output_name", type=str, default="_", help="Name of the output color palette image. Default is the input file name plus added data.")
    parser.add_argument("--percentile", type=lambda x: check_range(x, 1, 100), default=15, help="Percentile for color extraction. 1-100. Default is 15. Lower percentile values tend to be darker and have more contrast.")

    args = parser.parse_args()

    file_name = args.image_path.split("/")[-1].split(".")[0]
    image = Image.open(args.image_path)
    colors = extract_palette(image, args.num_colors, args.percentile)
    
    os.makedirs(os.path.dirname(args.output_dir), exist_ok=True)

    output_path = ""
    if args.output_name == "_":
        output_path = f"{args.output_dir}{file_name}-palette-colors-{args.num_colors}-percentile-{args.percentile}.png"
    else:
        output_path = f"{args.output_dir}{args.output_name}.png"

    palette = create_color_palette(colors)
    save_palette(palette, output_path)

if __name__ == "__main__":
    main()