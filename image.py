class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, image_file):
        def to_byte(value):
            # make sure value is an integer between 0 and 255
            return round(max(min(value * 255, 255), 0))

        # write headers
        image_file.write('P3 {} {}\n255\n'.format(self.width, self.height))
        for row in self.pixels:
            for color in row:
                image_file.write('{} {} {} '.format(
                    to_byte(color.x), to_byte(color.y), to_byte(color.z))
                )
            image_file.write('\n')
