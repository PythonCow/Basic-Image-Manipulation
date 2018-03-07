from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

hex_color_to_replace = sys.argv[2]
color_to_replace = [int(i, 16) for i in [hex_color_to_replace[0:2], hex_color_to_replace[2:4], hex_color_to_replace[4:]]]

hex_color_to_add = sys.argv[3]
color_to_add = [int(i, 16) for i in [hex_color_to_add[0:2], hex_color_to_add[2:4], hex_color_to_add[4:]]]

tolerance = int(sys.argv[4])

new_rgblist = []

for i in range(image.height):
    new_rgblist.append([])
    for j in range(image.width):
        new_rgb = []
        color_matches = True
        for k in range(3):
            if abs(color_to_replace[k] - image.rgblist[i][j][k]) > tolerance:
                color_matches = False
                break
        if color_matches:
            for k in range(3):
                new_rgb.append(image.rgblist[i][j][k] + color_to_add[k])
                if new_rgb[k] > 255:
                    new_rgb[k] = 255
        else:
            new_rgb = image.rgblist[i][j]
        new_rgblist[i].append(new_rgb)

ppm(image.width, image.height, new_rgblist).write_to_file(sys.argv[5])
