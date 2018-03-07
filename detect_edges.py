from ppm import *
import sys

kernels = [
    [[1, 0, -1], [0, 0, 0], [-1, 0, 1]],
    [[0, -1, 0], [-1, 4, -1], [0, -1, 0]],
    [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
]
ppm_from_file(sys.argv[1]).apply_kernel(kernels[int(sys.argv[2])]).write_to_file(sys.argv[3])
