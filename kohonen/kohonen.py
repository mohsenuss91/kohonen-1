from PIL import Image
import random
from math import floor, ceil, sqrt

ITER = 20;
path = "images/bear.jpg"
im = Image.open(path)
image = im.load()
dim = im.size


# Centroids
classes = int(raw_input("How many colors? "));
centroids = []

a = int(round(sqrt((classes*dim[0])/dim[1])))
b = int(round(sqrt((classes*dim[1])/dim[0])))

width = dim[0] // a
height = dim[1] // b
count = 0

for i in xrange(a):
	for j in xrange(b):
		if count < classes:
			x = random.randint(i*width, (i+1)*width)
			y = random.randint(j*height, (j+1)*height)
			pixel = list(image[x,y])
			centroids.append(pixel)
			count += 1
for i in xrange(a):
	for j in xrange(b):
		if count < classes:
			x = random.randint(i*width, (i+1)*width)
			y = random.randint(j*height, (j+1)*height)
			pixel = list(image[x,y])
			centroids.append(pixel)
			count += 1

print "Centroids: ", centroids
print "Dimensions: ", dim
width = int(dim[0])
height = int(dim[1])

if width % 2 is 0:
	width -= 1
if height % 2 is 0:
	height -= 1
print "Dimensions: ", width, height
count = 0
height -= 1
width -= 1
for q  in xrange(2, ITER):
	# Moving inside the image.
	for i in xrange(width):
		for j in xrange(height):
			minimum = 10e4

			if j % 2 is 0:
				pixel = image[i, j]
			if (height-j) % 2 is 1:
				print height-i, "and ", height-j
				pixel = image[height-i, height-j]

			for k in xrange(classes):
				distance = pow(pixel[0] - centroids[k][0], 2) + pow(pixel[1] - centroids[k][1], 2) + pow(pixel[2] - centroids[k][2], 2)
				if distance < minimum:
					minimum = distance
					cPoint = k
			centroids[cPoint][0] += ((pixel[0] - centroids[cPoint][0]) / q)
			centroids[cPoint][1] += ((pixel[1] - centroids[cPoint][1]) / q)
			centroids[cPoint][2] += ((pixel[2] - centroids[cPoint][2]) / q)

print "Moved centroids ", centroids

# Working demo

for i in xrange(dim[0]):
	for j in xrange(dim[1]):
		minimum = 10e4
		pixel = image[i, j]
		for k in xrange(classes):
			distance = pow(pixel[0] - centroids[k][0], 2) + pow(pixel[1] - centroids[k][1], 2) + pow(pixel[2] - centroids[k][2], 2)
			if distance < minimum:
				minimum = distance
				cPoint = k
		image[i, j] = (centroids[cPoint][0], centroids[cPoint][1], centroids[cPoint][2])

im.save("opt.jpg")

