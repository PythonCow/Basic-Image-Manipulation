from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

new_rgblist = [i[::-1] for i in image.rgblist]

ppm(image.width, image.height, new_rgblist).write_to_file(sys.argv[2])
