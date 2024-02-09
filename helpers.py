# this is the collection of helper functions for python scripts

# simple picture resizing function
from PIL import Image
import os
def resize_pictures(org_folder, resized_folder):

    if not os.path.exists(resized_folder):
        os.mkdir(resized_folder)

    for pic in os.listdir(org_folder):
        if os.path.isfile(os.path.join(org_folder, pic)):
            print(f"Working with file {pic}")
            extension = str(pic).split(".")[-1]
            name = str(pic).split(".")[0]
            print(f"name: {name}, extension: {extension}")
            img = Image.open(os.path.join(org_folder, pic))
            img_resized = img.resize((500,500))
            img_resized.save(os.path.join(resized_folder, name + "_resized." + extension))

# resize_pictures("images", "resized")



