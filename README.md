# Random Image Combiner

## Overview
The Image Combiner is a Python script that generates a specified number of random combined images by layering images from different folders. Users can customize the size of the images, the folders from which the images will be selected, and the target folder where the combined images will be saved.

## Features
- Combine images from multiple folders into layered images.
- Customize the number of images to generate and their size.
- Check for the existence of specified folders and handle errors.
- Save the final combined images in a designated target folder.

## Requirements
- Python 3.x
- Pillow library for image processing
- JSON file for configuration

## Installation
1. Clone or download this repository.
2. Install the Pillow library if you haven't already. You can do this using pip:
bash
   pip install Pillow

## Configuration
Create or edit a settings.json file in the same directory as the script. The file should have the following structure:

{
    "Range": 1500,
    "Size": [105, 105],
    "Folders": ["backgrounds", "body", "etc", "hats", "additional"],
    "TargetFolder": "ready"
}

## Explanation of Settings:
1. Range: The number of images that will be generated.
2. Size: The width and height of the images as an array (e.g., [105, 105]).
3. Folders: A list of folder names where the images are stored. The order of the folders matters as it determines the layering of the images.
4. TargetFolder: The folder where the generated combined images will be saved.

## Usage 
1. Ensure you have the appropriate folders with images created in the same directory as the script:
2. Run the script:
    python generate.py
3. The script will check for the existence of the specified folders. If any folder is missing, an error message will be displayed.
4. Once the process is complete, the combined images will be saved in the specified target folder.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
 
## Contact
For any questions or issues, please contact Daniel at dnlradziak@gmail.com.