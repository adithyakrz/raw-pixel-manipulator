import numpy as np
import matplotlib.pyplot as pyplot
img = pyplot.imread("./input.jpg")
pyplot.imshow(img)
pyplot.show()

print ("Shape = ",img.shape)
print("Data type = ",img.dtype)
print("Min pixel = ",img.min(),"\nMax pixel = ",img.max())