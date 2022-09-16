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
from light import Light
from material import Material
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('imageout', help='Path to rendered image')
    args = parser.parse_args()

    WIDTH = 1024
    HEIGHT = 720
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.2, Material(Color.from_hex('#FF0000')))]
    lights = [Light(Point(3, -8, -10.0), Color.from_hex('#FFFFFF'))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open(args.imageout, 'w') as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()
