import sys
import os
from PIL import Image

# grab first and second arguments
OLD_folder = sys.argv[1]
SAVE_folder = sys.argv[2]
#check if new/ exists, if not create
if os.path.isdir(SAVE_folder) == False:
    os.mkdir(SAVE_folder)
    print(f'Folder {SAVE_folder} was created')
else:
    print(f'Folder {SAVE_folder} already exist')
#loop through Pokedex
for each_image in os.listdir(OLD_folder):
    photoName = each_image
    if each_image.lower().endswith('.jpg'):
        image_path = os.path.join(OLD_folder,photoName)
        img = Image.open(image_path)

        save_path = os.path.join(SAVE_folder,photoName[:-4]+ '.png')
        img.save(save_path)
    else:
        print('Support JPG file only')
#convert images to png
#save to the new folder



