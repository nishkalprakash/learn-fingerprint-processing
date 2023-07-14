import cv2

#randamize the image
from numpy import random
from PIL import Image
arr = random.rand(512, 512, 3)*255
random_img = Image.fromarray(arr.astype('uint8')).convert('RGBA')
random_img.save('file.png')


#using the cv2 module now
img_rgb = cv2.imread('rose.png')
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',img_rgb)
cv2.imshow('Gray image', img_gray)
 # rgb value 
cv2.waitKey(0)
cv2.destroyAllWindows()