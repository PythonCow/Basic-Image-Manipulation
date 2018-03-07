import random
import math

dimy = 800
dimx = 800
file = open('test.ppm', 'br+')

file.write(b'P6\n' + bytes(str(dimx), 'ascii') + b' ' + bytes(str(dimx), 'ascii') + b'\n255\n')

for i in range(dimx):
    for j in range(dimy):
        file.write(bytes([ math.floor(i * (256 / dimy)), math.floor(j * (256 / dimx)), random.randint(0, 255)]))

file.close()
