import numpy as np
import matplotlib.pyplot as pyplot
from filters import toGrayScale,adjustBrightness

img = pyplot.imread("./input.jpg")
pyplot.imshow(img)
pyplot.show()

print ("Shape = ",img.shape)
print("Data type = ",img.dtype)
print("Min pixel = ",img.min(),"\nMax pixel = ",img.max())

gray = toGrayScale(img)

print("GrayScale image shape: ",img.shape)
print("GrayScale image shape: ",gray.shape)

pyplot.imshow(gray,cmap="gray")
pyplot.title("Gray Scale image")
pyplot.show()

brightimg = adjustBrightness(img, 50)
pyplot.imshow(brightimg)
pyplot.title("Bright image (+50)")
pyplot.show()