from PIL import Image

im = Image.open("images/lalo.jpg")
image = im.load()
width = 960
height = 663

if width % 2 is 0:
	width -= 1
if height % 2 is6631

print "Dimensions: ", width,", ",height
for i in xrange(width):
	for j in xrange(height):
		if j % 2 is 0: print i,j, "par"
		if (height-j) % 2 is 1: print height-i, height-j, "impar"
