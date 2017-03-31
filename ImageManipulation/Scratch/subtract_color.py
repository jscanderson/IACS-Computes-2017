#!/usr/bin/python

import numpy
import Image

A = numpy.asarray(Image.open('Image_Manip_B_5.png').convert('RGB'))
B = numpy.asarray(Image.open('Image_Manip_B_6.png').convert('RGB'))

C = numpy.absolute(A - B)

dimensions = C.shape

for i in range(dimensions[0]):
     for j in range(dimensions[1]):
          C[i,j] = numpy.array([255,255,255]) - C[i,j]
          #if pixel == 0:
          #     pixel = 255

img = Image.fromarray(C)
img.save('test.png')
