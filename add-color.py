from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

hex_color = sys.argv[2]

color = [int(i, 16) for i in [hex_color[0:2], hex_color[2:4], hex_color[4:]]]

new_rgblist = []

for i in range(image.height):
    new_rgblist.append([])
    for j in range(image.width):
        new_rgb = []
        for k in range(3):
            new_rgb.append(image.rgblist[i][j][k] + color[k])
            if new_rgb[k] > 255:
                new_rgb[k] = 255
        new_rgblist[i].append(new_rgb)

ppm(image.width, image.height, new_rgblist).write_to_file(sys.argv[3])
