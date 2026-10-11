import numpy as np
import matplotlib.pyplot as pyplot
from filters import tograyscale

img = pyplot.imread("./input.jpg")
pyplot.imshow(img)
pyplot.show()

print ("Shape = ",img.shape)
print("Data type = ",img.dtype)
print("Min pixel = ",img.min(),"\nMax pixel = ",img.max())

gray = tograyscale(img)

print("GrayScale image shape: ",img.shape)
print("GrayScale image shape: ",gray.shape)

pyplot.imshow(gray,cmap="gray")
pyplot.show()