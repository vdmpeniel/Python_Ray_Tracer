#!/usr/bin/env python
# this is called a shabang and it is used to make this file executable

# all this boilerplate code is called the shell,
# and it is used to execute main

""" A Pure Python Raytracer by Victor Diaz, 2022,
    based on Arun Ravidran video series
"""
from image import Image
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine



def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.2, Color.from_hex('#FF0000'))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open('test.ppm', 'w') as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()
