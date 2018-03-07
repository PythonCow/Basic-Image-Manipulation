from ppm import *
import sys

image = ppm_from_file(sys.argv[1])

blurriness = int(sys.argv[2])

new_rgblist = []

for i in range(image.height):
    new_rgblist.append([])
    for j in range(image.width):
        new_rgb = []
        left_distance = right_distance = up_distance = down_distance = blurriness
        if j < left_distance + 1:
            right_distance = j
        if (image.width - 1) - j < right_distance:
            right_distance = (image.width - 1) - j
        if i < up_distance + 1:
            up_distance = i
        if (image.height - 1) - i < down_distance:
            down_distance = (image.height - 1) - i
        for k in range(3):
            total = image.rgblist[i][j][k] * (.2)
            for l in range(1, left_distance):
                total += image.rgblist[i][j - l][k] * (.2 / (left_distance - 1))
            for l in range(1, right_distance):
                total += image.rgblist[i][j + l][k] * (.2 / (right_distance - 1))
            for l in range(1, up_distance):
                total += image.rgblist[i - l][j][k] * (.2 / (up_distance - 1))
            for l in range(1, down_distance):
                total += image.rgblist[i + l][j][k] * (.2 / (down_distance - 1))
            new_rgb.append(int(total)) #// ((left_distance - 1) + (right_distance - 1) + (up_distance + 1) + (down_distance + 1) + 1))
        new_rgblist[i].append(new_rgb)

ppm(len(new_rgblist[1]), len(image.rgblist), new_rgblist).write_to_file(sys.argv[3])
