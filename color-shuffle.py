from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

new_rgblist = []

for i in range(image.height):
    new_rgblist.append([])
    for j in range(image.width):
        new_rgblist[i].append(image.rgblist[i][j][1:] + [image.rgblist[i][j][0]])

ppm(image.width, image.height, new_rgblist).write_to_file(sys.argv[2])
