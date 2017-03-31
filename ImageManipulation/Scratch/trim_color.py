#!/usr/bin/python

import numpy
import Image

endname = 'Image_Manip_J_6.png'

A = numpy.asarray(Image.open('Image_Manip_J_2.png').convert('RGB'))

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
while all(A[temp,column] == [255,255,255]):
     temp = temp+1
temp = temp-1
rowstart = temp


#fix bottom
temp = bottom
while all(A[temp,column] == [255,255,255]):
     temp = temp-1
temp = temp+1
rowend = temp

#fix left
temp = 0
while all(A[row,temp] == [255,255,255]):
     temp = temp+1
temp=temp-1
colstart = temp

#fix right
temp = right
while all(A[row,temp] == [255,255,255]):
     temp = temp-1
temp = temp+1
colend = temp

D = A[rowstart:rowend,colstart:colend]
img = Image.fromarray(D)
img.save(endname)



#kthxbye
