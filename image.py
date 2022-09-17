class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    @staticmethod
    def write_ppm_header(img_file_obj, height=None, width=None):
        """Write only the header of a PPM file"""
        img_file_obj.write('P3 {} {}\n255\n '.format(width, height))

    def write_ppm_raw(self, image_file_obj):
        def to_byte(value):
            # make sure value is an integer between 0 and 255
            return round(max(min(value * 255, 255), 0))

        for row in self.pixels:
            for color in row:
                image_file_obj.write('{} {} {} '.format(
                    to_byte(color.x), to_byte(color.y), to_byte(color.z))
                )
            image_file_obj.write('\n')

    def write_ppm(self, img_file_obj):
        Image.write_ppm_header(img_file_obj, height=self.height, width=self.width)
        self.write_ppm_raw(img_file_obj)
