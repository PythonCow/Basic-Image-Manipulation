from ppm import *
import sys
import math

image = ppm_from_file(sys.argv[1])

new_rgblist = []

for i in range(image.height):
    new_rgblist.append([])
    for j in range(image.width):
        new_rgblist[i].append([math.floor(abs(math.sin(1 / (k + 1)) * 255)) for k in image.rgblist[i][j]])

ppm(image.width, image.height, new_rgblist).write_to_file(sys.argv[2])
