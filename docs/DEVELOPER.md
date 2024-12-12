# Developer Guide for imagRGB

## Overview

The `imagRGB` project is designed to extract color palettes from images using K-Means clustering and percentile-based centroids. The project includes both a graphical user interface (GUI) using Streamlit and a command-line interface (CLI). The main files in this project are:

- [main.py](../main.py): Contains the core functionality for extracting and saving color palettes.
- [app.py](../app.py): Implements the Streamlit GUI for user interaction.
- [requirements.txt](../requirements.txt): Lists the dependencies required to run the project.

## File Interactions

- [main.py](../main.py): This file contains the core logic for extracting color palettes from images. It includes functions for extracting colors, creating a palette image, and saving the palette.
- [app.py](../app.py): This file sets up the Streamlit app, allowing users to upload images, adjust parameters, and download the generated color palette.
- [requirements.txt](../requirements.txt): Lists the required Python packages for the project.

## Explanation of `app.py`

The [app.py](../app.py) file uses Streamlit to create a web-based interface for the `imagRGB` project. Here's a high-level overview of how it works:

1. **Streamlit Configuration**: The app is configured with a title and layout using `st.set_page_config`.
2. **File Upload**: Users can upload an image file using `st.file_uploader`.
3. **Image Display**: The uploaded image is displayed using `st.image`.
4. **Sliders for Parameters**: Users can adjust the number of colors and the percentile for color extraction using `st.slider`.
5. **Tooltip**: A tooltip provides additional information about the percentile parameter.
6. **Color Extraction and Palette Creation**: The uploaded image is processed to extract colors and create a color palette using functions from [main.py](../main.py).
7. **Palette Display and Download**: The generated color palette is displayed and can be downloaded using `st.download_button`.

## Explanation of `main.py` Methods

- **`extract_palette(image, n_colors, percentile)`**: Extracts a color palette from an image using K-Means clustering and percentile-based centroids. Converts the image to OpenCV format, applies K-Means clustering, and calculates the percentile-based centroids.

- **`create_color_palette(colors)`**: Creates an image of a color palette from a list of colors. Draws rectangles for each color and adds text labels for RGB, HEX, and CMYK values.

- **`save_palette(palette, output_path)`**: Saves the color palette image to the specified path.

- **`check_range(value, min_val, max_val)`**: Validates that a value is within a specified range. Used for argument parsing.

- **`main()`**: The main function to generate a color palette from an image. Parses command-line arguments, extracts colors, creates a palette, and saves the palette image.

## Useful Links

- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [NumPy Documentation](https://numpy.org/doc/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

This guide provides a high-level overview of the `imagRGB` project and its main components. For detailed usage instructions, refer to the [README.md](../README.md) file.
