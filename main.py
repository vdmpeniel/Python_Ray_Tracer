#!/usr/bin/env python
# this is called a shabang and it is used to make this file executable

# all this boilerplate code is called the shell,
# and it is used to execute main

""" A Pure Python Raytracer by Victor Diaz, 2022,
    based on Arun Ravidran video series
"""
from image import Image
from color import Color


def main():
    WIDTH = 3
    HEIGHT = 2
    image = Image(WIDTH, HEIGHT)
    red = Color(1, 0, 0)
    green = Color(0, 1, 0)
    blue = Color(0, 0, 1)

    image.set_pixel(0, 0, red)
    image.set_pixel(1, 0, green)
    image.set_pixel(2, 0, blue)

    image.set_pixel(0, 1, red + green)
    image.set_pixel(1, 1, red + blue + green)
    image.set_pixel(2, 1, red * 0.001)

    with open('test.ppm', 'w') as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()
