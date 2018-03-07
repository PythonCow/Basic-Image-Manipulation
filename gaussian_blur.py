from ppm import *
import sys
import math

standard_deviation = int(sys.argv[2])
distance = int(sys.argv[3])
kernel_width = (distance * 2) + 1
center_index = (kernel_width // 2)

def gaussian_function(x, y):
    return math.exp(-(x ** 2 + y ** 2) / (2 * standard_deviation ** 2)
                    ) / (2 * math.pi * standard_deviation ** 2)


kernel = []
total = 0

for i in range(kernel_width):
    kernel.append([])
    for j in range(kernel_width):
        weight = gaussian_function(j - center_index, i - center_index)
        total += weight
        kernel[i].append(weight)

for i in range(len(kernel)):
    for j in range(len(kernel[i])):
        kernel[i][j] = round(kernel[i][j] / total, 6)

[print(i) for i in kernel]
print(sum([sum([j for j in i]) for i in kernel]))
image = ppm_from_file(sys.argv[1])
image.apply_kernel(kernel).write_to_file(sys.argv[4])
