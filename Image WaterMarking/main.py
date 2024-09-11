import os
from PIL import Image

def watermark_photo(image_path, watermark_path, output_path):
    base_image = Image.open(image_path)
    watermark = Image.open(watermark_path).convert("RGBA")
    
    # Get the size of the base image
    position = base_image.size
    
    # Maintain watermark's aspect ratio
    watermark_aspect_ratio = watermark.width / watermark.height
    new_width = int(position[0] * 8 / 100)
    new_height = int(new_width / watermark_aspect_ratio)
    newsize = (new_width, new_height)
    
    # Resize the watermark
    watermark = watermark.resize(newsize)
    
    # Calculate position to paste the watermark
    new_position = (position[0] - newsize[0] - 20, position[1] - newsize[1] - 20)
    
    # Create a transparent image to hold the base image and watermark
    transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, new_position, watermark)
    
    # Convert to original image mode before saving
    image_mode = base_image.mode
    if image_mode == "RGB":
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P')
    
    # Save the output
    transparent.save(output_path, optimize=True, quality=100)
    print(f"Saved watermarked image as {output_path}")

# Get user input for folder and watermark
folder = input("Enter Folder Path: ")
watermark = input("Enter Watermark Path: ")

# Change directory to the specified folder
os.chdir(folder)

# List all files in the directory
files = os.listdir(os.getcwd())
print("Files in the directory:", files)

# Create output folder if it doesn't exist
if not os.path.isdir("output"):
    os.mkdir("output")

# Loop through files and apply watermark
for f in files:
    if os.path.isfile(f):
        print(f"Processing file: {f}")  # Debugging statement
        if f.endswith(".png") or f.endswith(".jpg"):
            print(f"Watermarking {f}...")  # Debugging statement
            watermark_photo(f, watermark, "output/" + f)
        else:
            print(f"Skipped non-image file: {f}")
    else:
        print(f"Skipped directory or non-file: {f}")
