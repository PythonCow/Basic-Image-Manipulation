
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
                       bytes(str(self.width), 'ascii') +
                       b' ' +
                       bytes(str(self.height), 'ascii') +
                       b'\n255\n')

        for i in range(self.height):
            for j in range(self.width):
                ppm_file.write(bytes(self.rgblist[i][j]))

        ppm_file.close()

    def apply_kernel(self, kernel):
        assert(len(kernel) % 2 == 1 and len(kernel[0]) % 2 == 1)

        def rgb_at_indices(x, y):
            if y < 0:
                y = 0
            if x < 0:
                x = 0
            if y > len(self.rgblist) - 1:
                y = len(self.rgblist) - 1
            if x > len(self.rgblist[y]) - 1:
                x = len(self.rgblist[y]) - 1
            return self.rgblist[y][x]

        new_rgblist = []
        for i in range(self.height):
            new_rgblist.append([])
            for j in range(self.width):
                print(((i * self.width) + j + 1) / (self.height * self.width) * 100)
                new_rgb = []
                for k in range(3):
                    accumulator = 0
                    for ymodifier in range(-(len(kernel) // 2), (len(kernel) // 2) + 1):
                        for xmodifier in range(-(len(kernel[0]) // 2), (len(kernel[0]) // 2) + 1):
                            accumulator += int(rgb_at_indices(j + xmodifier, i + ymodifier)[k]
                                               * kernel[ymodifier + (len(kernel) // 2)]
                                               [xmodifier + (len(kernel[0]) // 2)])
                    #Sometimes kernels have negative numbers and the total can come out negative, obviously we can't have that.
                    if accumulator < 0: accumulator = 0
                    if accumulator > 255: accumulator = 255
                    new_rgb.append(accumulator)
                new_rgblist[i].append(new_rgb)
        return ppm(self.width, self.height, new_rgblist)


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


if __name__ == '__main__':
    '''width = 255
    height = 255
    rgblist = []

    for i in range(height):
        rgblist.append([])
        for j in range(width):
            rgblist[i].append([i, 255, j])

    new_image = ppm(width, height, rgblist)
    new_image.write_to_file('test1.ppm')

    ppm_from_file('dog_getting_hit_by_frisbee.ppm').write_to_file('test2.ppm')'''

    shrek = ppm_from_file('ozzy.ppm')
    kernel = [[1, 4, 6, 4, 1]]
    shrek.apply_kernel([[j / 16 for j in i] for i in kernel]).write_to_file('blurry_ozzy.ppm')
