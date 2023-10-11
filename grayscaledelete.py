#Deletes any black and white/grayscale images from a folder
import os
from PIL import Image, ImageStat
from functools import reduce

MONOCHROMATIC_MAX_VARIANCE = 0.005
COLOR = 1000
MAYBE_COLOR = 100

def detect_color_image(file):
    v = ImageStat.Stat(Image.open(file)).var
    is_monochromatic = reduce(lambda x, y: x and y < MONOCHROMATIC_MAX_VARIANCE, v, True)
    print(file, '-->')
    if is_monochromatic:
        print("Monochromatic image")
    else:
        if len(v) == 3:
            maxmin = abs(max(v) - min(v))
            if maxmin > COLOR:
                print("Color\t\t\t")
            elif maxmin > MAYBE_COLOR:
                print("Maybe color\t")
            else:
                print("grayscale\t\t")
                os.remove(file)  # Delete the grayscale image
                print(f"Deleted {file}")
                return
            print("(", maxmin, ")")
        elif len(v) == 1:
            print("Black and white")
            os.remove(file)  # Delete the grayscale image
            print(f"Deleted {file}")
        else:
            print("Don't know...")
#DIRECTORY PATH HERE
directory_path = "your/path"

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
        try:
            detect_color_image(file_path)
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
