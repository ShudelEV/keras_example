import os
from imutils import paths

media_dir = "/media/disk2/users"
images = paths.list_images(media_dir)

for img in images:
    img_dir, img_name = os.path.split(img)
    os.replace(img, os.path.join("/media/disk2", "output", img_name))
