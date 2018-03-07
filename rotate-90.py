from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

new_rgblist = []

for i in range(image.width):
    new_rgblist.append([])
    for j in range(image.height):
        new_rgblist[i].append(image.rgblist[j][i])

ppm(image.height, image.width, new_rgblist).write_to_file(sys.argv[2])
