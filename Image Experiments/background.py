from PIL import Image
import os
import numpy as np
from preprocess import transform_image

def get_background_images(IMAGE_PATH):
        
        fish_images = list()
        for filename in os.listdir(IMAGE_PATH):
                if filename.endswith(".JPEG") or filename.endswith(".JPG") or filename.endswith(".jpg"):
                        try:
                                img = Image.open(os.path.join(IMAGE_PATH, filename))
                                img = img.convert(mode="L") # grayscale
                                img = transform_image(img) # resize and crop
                                fish_images.append(np.reshape(img, [10000])) 
                        except Exception as e:
                                pass
        fish_images = np.asarray(fish_images,dtype=float)
        fish_images /= 255
        print("Dim of fish images: ", fish_images.shape)
        return fish_images
