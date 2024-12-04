# imagRGB
Project for converting images to color palettes. Fall-2024-HCI-584

## Dependencies and Running the Project
To run this project you will need the following installed:
- Pillow
- numpy
- scikit-learn
- opencv-python

A [requirements.txt](./requirements.txt) file is included in the project, so you can install these libraries by running `pip install -r requirements.txt` from the root of the project.

### Run with CLI

Run the application by running [main.py](./main.py): `python main.py [IMAGE_PATH]`. You must provide the image path as a positional argument. You can provide other optional arguments to adjust the output. Run `python main.py --help` for a list of arguments.
```
usage: main.py [-h] [--num_colors NUM_COLORS] [--output_dir OUTPUT_DIR] [--output_name OUTPUT_NAME] [--percentile PERCENTILE] image_path

Generate a color palette from an image.

positional arguments:
  image_path            Path to the input image file.

options:
  -h, --help            show this help message and exit
  --num_colors NUM_COLORS
                        Number of colors to extract from the image. 1-10. Default is 5.
  --output_dir OUTPUT_DIR
                        Directory to save the color palette image. Default is ./palettes/
  --output_name OUTPUT_NAME
                        Name of the output color palette image. Default is the input file name plus added data.
  --percentile PERCENTILE
                        Percentile for color extraction. 1-100. Default is 15. Lower percentile values tend to be darker and have more contrast.
```

### Run Streamlit GUI App

Start a locally hosted streamlit app by running `streamlit run app.py` or `python -m streamlit app.py`.

## Attribution
- [Example images](./example-images/) in this project were sourced from [https://unsplash.com/](https://unsplash.com/)