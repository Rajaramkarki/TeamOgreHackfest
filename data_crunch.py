from ast import main
import numpy as np
from PIL import ImageTk, Image, ImageChops, ImageOps , ImageEnhance
import cv2

im0 = Image.open(r"C:\Users\97798\Documents\TeamOgreHackfest\data\gee_slope.jpg")
im1 = Image.open(r"C:\Users\97798\Documents\TeamOgreHackfest\data\gee_rainfall.jpg")
im2 = Image.open(r"C:\Users\97798\Documents\TeamOgreHackfest\data\gee_soil.jpg")

# im0 = ImageOps.invert(im0)
# im1 = ImageOps.invert(im1)

# PIL.ImageChops.multiply() method superimposes two images on top of each other.
# If you multiply an image with a solid black image, the result is black.
# If you multiply with a solid white image, the image is unaffected. 
# At least one of the images must have mode “1”.

im = ImageChops.multiply(im2,im1)
im = ImageChops.multiply(im,im0)

im.show()

