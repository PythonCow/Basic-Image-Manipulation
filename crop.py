from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

x = int(sys.argv[3])
y = int(sys.argv[4])
width = int(sys.argv[5])
height = int(sys.argv[6])
new_rgblist = []

for i in range(y, y + height):
    new_rgblist.append([])
    for j in range(x, x + width):
        new_rgblist[i - y].append(image.rgblist[i][j])

ppm(width, height, new_rgblist).write_to_file(sys.argv[2])
