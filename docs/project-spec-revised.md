# imagRGB: Revised Project Specification

## 1. General Description of the Project

**imagRGB** is a Python-based application that generates customizable color palettes from user-provided images. The application is aimed at designers, artists, and developers, and extracts dominant colors from images to inspire and inform creative projects. The core feature involves analyzing an image to identify the most prevalent colors and presenting them with detailed information, enhancing the user's ability to incorporate these colors into their work.

**Key Features:**

- **Dominant Color Extraction:** Identifies the most significant colors in an image.
- **Customizable Output:** Users can specify the number of colors in the palette.
- **Detailed Color Information:** Displays color names, HEX codes, RGB values, and CMYK values.
- **User Interfaces:** Offers both a **Graphical User Interface (GUI)** via Streamlit and a **Command-Line Interface (CLI)** for different types of users.
- **Palette Saving and Exporting (Revised):** Allows users to save and download color palettes for future use. Color palettes will be in the form of a PNG or JSON data.
- **Friendly Color Naming (Revision - Removed):** The feature to provide friendly color naming labels has been removed from the scope due to the unavailability of a suitable third-party library and the challenges involved in performing this analysis accurately.

**Nice-to-Have Features (Revision - Time Permitting):**

- **Post-Processing Options:** Adjustments such as brightness and saturation are considered "nice-to-have" but may be added if time permits.
- **Ordered Color Presentation:** Colors can be displayed in meaningful sequences, such as by dominance or hue.

**Dropped Features (Revision):**

- The initial plan to integrate **API/remote control functionality** and **image capture via webcam or mobile device** has been dropped to focus on the primary interfaces.

**User Interface:**

- **Graphical User Interface (GUI):** Developed using Streamlit for an intuitive, easy-to-use experience.
- **Command-Line Interface (CLI):** Support for users who prefer non-GUI environments.

**External Libraries and Packages:**

- **Pillow (PIL):** Used for image loading and basic processing.
- **NumPy:** Enables efficient numerical computations.
- **scikit-learn:** Utilized for K-Means clustering to identify dominant colors.
- **Webcolors (Revision - Removed):** Initially planned to map RGB values to official color names; however, it turned out not to be sufficient for getting friendly color names directly.

## 2. Task Vignettes (Not Materially Revised)

### Vignette 1: Generating a Basic Color Palette

**Narrative:**

Emma, a graphic designer, wants to create a color scheme inspired by a photograph. She opens imagRGB and selects her image using the "Upload Image" button. She inputs "5" for the number of dominant colors and clicks "Generate Palette." The application displays the top five colors with their HEX and RGB values. Emma downloads the palette as an image file for her design software.

**Technical Details:**

- **User Inputs:**
  - Image file via upload.
  - Number of colors (integer).
- **Processing Steps:**
  - Load image with Pillow.
  - Resize for efficiency.
  - Extract colors using K-Means clustering.
  - Convert RGB to HEX codes.
- **Outputs:**
  - Color swatches displayed in order of dominance.
  - Color codes presented alongside swatches.
  - Option to download the palette image.

### Vignette 2: Customizing Color Information and Adjustments

**Narrative:**

Carlos, a web developer, needs CMYK values and lighter shades. He accesses "Advanced Options" in imagRGB, enables CMYK display, and adjusts brightness by +10%. The updated palette shows adjusted colors with HEX, RGB, and CMYK codes. Carlos copies the codes into his style guide.

**Technical Details:**

- **User Inputs:**
  - Selection of CMYK display.
  - Brightness adjustment slider.
- **Processing Steps:**
  - Adjust RGB values for brightness.
  - Convert adjusted RGB to CMYK.
  - Update display with new values.
- **Outputs:**
  - Adjusted color swatches.
  - Comprehensive color information.

## 3. Technical Flow (Not Materially Revised)

### Overall Data Flow Description

**Stages:**

1. **User Interaction Blocks:**

   - **Image Input Block:** User uploads or captures an image.
   - **Parameter Input Block:** User specifies settings (number of colors, adjustments).

2. **Processing Blocks:**

   - **Image Preprocessing Block:** Resizes image, converts color space.
   - **Color Extraction Block:** Identifies dominant colors using K-Means clustering.
   - **Color Adjustment Block:** Applies brightness/saturation changes.
   - **Color Mapping Block:** Converts RGB values to HEX, CMYK, assigns color names.

3. **Output Blocks:**

   - **Display Block:** Shows color palette and information.
   - **Save/Export Block:** Allows downloading palette and data.

**User Interaction Points**

- **Inputs:**
  - Upload/select images.
  - Enter parameters (number of colors, adjustments).
- **Outputs:**
  - Display generated palettes.
  - Download files.

