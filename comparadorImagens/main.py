# create a program that compare two images
# and return the difference

import cv2
import numpy as np

img1 = cv2.imread('image.jpg')
img2 = cv2.imread('image2.jpg')

# get the width and height of the image
img = cv2.imread('image.jpg')
h, w, c = img.shape
height = h
width = w

diff = cv2.subtract(img1, img2)

if diff.any():
    print('\nImagens são diferentes\n')
else:
    print('\nImagens são iguais\n')


errorL2 = cv2.norm(img1, img2, cv2.NORM_L2)
similarity = 1 - errorL2 / (height * width)
similarity = (str(similarity)[str(similarity).find(
    '.')+1:str(similarity).find('.')+3]+'%')

if similarity == '0%':
    similarity = '100%'
else:
    similarity = similarity

print('Similaridade = ', similarity+'\n')
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
