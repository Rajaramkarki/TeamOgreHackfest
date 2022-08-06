import numpy as np
from PIL import ImageTk, Image, ImageChops, ImageOps , ImageEnhance
import cv2

def binarize(img):

  #initialize threshold
  thresh=50

  #convert image to greyscale
  img=img.convert('L') 

  width,height=img.size

  #traverse through pixels 
  for x in range(width):
    for y in range(height):

      #if intensity less than threshold, assign white
      if img.getpixel((x,y)) < thresh:
        img.putpixel((x,y),0)

      #if intensity greater than threshold, assign black 
      else:
        img.putpixel((x,y),255)

  return img



im0 = Image.open("data\gee_slope.jpg")
im1 = Image.open("data\gee_rainfall.jpg")
im2 = Image.open("data\gee_soil.jpg")

# im0 = ImageOps.invert(im0)
# im1 = ImageOps.invert(im1)

# PIL.ImageChops.multiply() method superimposes two images on top of each other.
# If you multiply an image with a solid black image, the result is black.
# If you multiply with a solid white image, the image is unaffected. 
# At least one of the images must have mode “1”.

im = ImageChops.multiply(im2,im1)
im = ImageChops.multiply(im,im0)
bin_image = binarize(im)
bin_image.show()
bin_image.save("data\output.jpg")