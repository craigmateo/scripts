## resize images in folder/subfolders 

from PIL import Image
import os, sys

## add root directory path here:
rootdir = 'C:/Users/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ## optional - add marker to select which files to change
        if file.endswith("16x9.png"):
            file_path = os.path.join(subdir,file)
            
            im = Image.open(file_path)
            width, height = im.size
            if width == 2560 and height == 1440:
                print(file_path)

            
            imResize = im.resize(1280,720)
            imResize.save(file_path, 'PNG', quality=100)
        