import sys
import os
from PIL import Image

# grab first and second arguments
open_folder = sys.argv[1]
save_folder = sys.argv[2]
#check if new/ exists, if not create
if os.path.isdir(save_folder) == False:
    os.mkdir(save_folder)
    print(f'Folder {save_folder} was created')
else:
    print(f'Folder {save_folder} already exist')
#loop through Pokedex
for image in os.listdir(open_folder):
    photo_name = image
    if image.lower().endswith('.jpg'):
        image_path = os.path.join(open_folder,photo_name)
        img = Image.open(image_path)
        save_path = os.path.join(save_folder,photo_name[:-4]+ '.png')
        img.save(save_path)
    else:
        print('Support JPG file only')
#convert images to png
#save to the new folder



