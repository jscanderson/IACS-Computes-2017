#!/usr/bin/python

import numpy
import Image

endname = 'Image_Manip_C_4.png'

A = numpy.asarray(Image.open('Image_Manip_C_2.png').convert('L'))

#White is read as 255

#find dimensions:
dimensions = A.shape
#approximate coordinates of center and edges:
column = dimensions[0]/2
row  = dimensions[1]/2
bottom = dimensions[0] - 1
right = dimensions[1] - 1

#fix top
temp = 0
while A[temp,column] == 255:
     temp = temp+1
temp = temp-1
rowstart = temp


#fix bottom
temp = bottom
while A[temp,column] == 255:
     temp = temp-1
temp = temp+1
rowend = temp

#fix left
temp = 0
while A[row,temp] == 255:
     temp = temp+1
temp=temp-1
colstart = temp

#fix right
temp = right
while A[row,temp] == 255:
     temp = temp-1
temp = temp+1
colend = temp

B = A[rowstart:rowend,colstart:colend]

img = Image.fromarray(B)
img.save(endname)



#kthxbye
