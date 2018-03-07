from ppm import *
import sys

kernel = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]

ppm_from_file(sys.argv[1]).apply_kernel(kernel).write_to_file(sys.argv[2])
