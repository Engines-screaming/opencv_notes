import cv2
import numpy as np
import matplotlib.pyplot as plt


path = "../media/test_image.png"
img = cv2.imread(path)


# can access pixel values by row/col coords. rgb returns (R, G, B) and greyscale returns intensity
px = img[100,100]  # BGR at coords 100, 100
print(px)


# you can access the BGR values by specifying the index of the [B, G, R] list when slicing the img coords
px_blue = img[100, 100, 0]
px_green = img[100, 100, 1]
px_red = img[100, 100, 2]
print(px_blue, px_green, px_red)


# better pixel accessing methods:
print(img.item(100, 100, 0))  # getter

img.itemset((100, 100, 0), 100)  # better setting
print(img.item(100, 100, 0)) 


# Accessing image properties
print(f"image shape property (rows, cols, channels): {img.shape}")
print(f"total pixels: {img.size}")
print(f"image dtype: {img.dtype}")


# IMAGE ROI (regions of images)
pig_nose = img[120:170, 90:140]
img[70:120, 90:140] = pig_nose  # move the pig nose 50 pixels up
cv2.imwrite('../media/modify_roi.png', img)


# Channel splitting
b, g, r = cv2.split(img)  # cant view individual channels since intensities are just shown as greyscale
# img = cv2.merge((b,g,r))  # merge the channels back togetherds after you modify it

blue = img[:, :, 0] # channel splitting with numpy indexing
# img[:, :, 1] = 0  # easy way to set all channels to 0
# img[:, :, 2] = 0
# cv2.imshow('modified', img)  # show modified img
# cv2.waitKey(0)


# Borders for images

