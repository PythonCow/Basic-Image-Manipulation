from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

for i in range(len(image.rgblist)):
    for j in range(len(image.rgblist[i])):
        image.rgblist[i][j] = [sum(image.rgblist[i][j]) // 3] * 3

image.write_to_file(sys.argv[2])
