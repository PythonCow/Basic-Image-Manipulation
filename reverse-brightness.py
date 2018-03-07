from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

for i in range(len(image.rgblist)):
    for j in range(len(image.rgblist[i])):
        image.rgblist[i][j] = [255 - rgb for rgb in image.rgblist[i][j]]

image.write_to_file(sys.argv[2])
