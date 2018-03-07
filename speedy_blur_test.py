from ppm import *
import sys

kernel0 = [[0.091637, 0.105358, 0.1164, 0.123573, 0.126061, 0.123573, 0.1164, 0.105358, 0.091637]]
kernel1 = [[i] for i in kernel0[0]]

ppm_from_file(sys.argv[1]).apply_kernel(kernel0).apply_kernel(kernel1).write_to_file(sys.argv[2])
