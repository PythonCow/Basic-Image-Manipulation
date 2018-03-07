from ppm import *
import sys

image1 = ppm_from_file(sys.argv[1])
image2 = ppm_from_file(sys.argv[2])

assert(image1.width == image2.width and image1.height == image2.height)

rgblist = []

for i in range(image1.height):
    rgblist.append([])
    for j in range(image1.width):
        new_rgb = []
        for k in range(3):
            new_rgb.append(image1.rgblist[i][j][k] // 2 + image2.rgblist[i][j][k] // 2)
        rgblist[i].append(new_rgb)

ppm(image1.width, image1.height, rgblist).write_to_file(sys.argv[3])
