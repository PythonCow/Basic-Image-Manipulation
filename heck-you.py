import sys

class ppm ():
    def __init__(self, width, height, rgblist):
        assert(type(width) == int)
        assert(type(height) == int)
        assert(type(rgblist) == list)
        self.width = width
        self.height = height
        self.rgblist = rgblist

    def write_to_file(self, filename):
        ppm_file = open(filename, 'wb')

        ppm_file.write(b'P6\n' +
                       bytes(str(self.height), 'ascii') +
                       b' ' +
                       bytes(str(self.width), 'ascii') +
                       b'\n255\n')

        for i in range(self.height):
            for j in range(self.width):
                ppm_file.write(bytes(self.rgblist[i][j]))

        ppm_file.close()


def ppm_from_file(filename):
    ppm_file = open(filename, 'br+')

    ppm_file_lines = ppm_file.readlines()

    width = int(ppm_file_lines[1].split(b' ')[0])
    height = int(ppm_file_lines[1].split(b' ')[1])
    rgblist = []

    count = 0
    encoded_rgbs = b''.join(ppm_file_lines[3:])
    for i in range(height):
        rgblist.append([])
        for j in range(width):
            rgb_encoded = encoded_rgbs[count * 3: (count * 3) + 3]
            rgblist[i].append([int(i) for i in rgb_encoded])
            count += 1

    return ppm(width, height, rgblist)

ppm_from_file(sys.argv[1]).write_to_file(sys.argv[2])
