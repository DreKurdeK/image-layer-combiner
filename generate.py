import random
import os
import json
from PIL import Image

# Function to read settings from a JSON file
def read_settings(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Load settings from the settings.json file
settings = read_settings('settings.json')

# Process the settings
range_limit = settings['Range']
size = tuple(settings['Size'])
folders = settings['Folders']
target_folder = settings['TargetFolder']

# Check if each folder exists
for folder in folders:
    folder_path = os.path.join('./' + folder)
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Error: The folder '{folder_path}' does not exist.")

# Create the target folder if it doesn't exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Main loop to combine images
for x in range(range_limit):
    
    # Start with the first image from the first folder
    base_image = Image.open(os.path.join('./' + folders[0], random.choice(os.listdir('./' + folders[0])))).resize(size)

    # Loop through the remaining folders to combine images
    for folder in folders[1:]:
        next_image = Image.open(os.path.join('./' + folder, random.choice(os.listdir('./' + folder)))).resize(size)
        base_image = Image.alpha_composite(base_image.convert('RGBA'), next_image.convert('RGBA'))

    # Save the final combined image in the specified target folder
    base_image.save(os.path.join(target_folder, f'final{x}.png'))

print("Finished combining images.")  # Indicate that the process is complete
