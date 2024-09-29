from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

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

def main():
    IMAGE_PATH = "example-images/fog-mountain-green-landscape.jpg"
    NUM_COLORS = 4

    colors = extract_colors(IMAGE_PATH, NUM_COLORS)
    
    print(f"Dominant colors in {IMAGE_PATH}:")
    for color in colors:
        print(f"RGB: {tuple(color)}")

if __name__ == "__main__":
    main()