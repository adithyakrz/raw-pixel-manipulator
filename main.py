import numpy as np
import matplotlib.pyplot as pyplot
from filters import toGrayScale,adjustBrightness,adjustContrast,flipImage

img = pyplot.imread("./input.jpg")

print("Shape = ",img.shape)
print("Data type = ",img.dtype)
print("Min pixel = ",img.min(),"\nMax pixel = ",img.max())

gray = toGrayScale(img)

print("GrayScale image shape: ",img.shape)
print("GrayScale image shape: ",gray.shape)

gray = toGrayScale(img)
print("Original image shape: ", img.shape)
print("GrayScale image shape: ", gray.shape)
pyplot.imsave("./output/output_gray.png", gray, cmap="gray")

brightimg = adjustBrightness(img, 50)
pyplot.imsave("./output/output_bright.png", brightimg)

contrastimg = adjustContrast(img, 1.5)
pyplot.imsave("./output/output_contrast.png", contrastimg)

flip = flipImage(img, "Vertical")
pyplot.imsave("./output/output_flip_v.png", flip)

flip = flipImage(img, "Horizondal")
pyplot.imsave("./output/output_flip_h.png", flip)

print("All output images saved successfully!")