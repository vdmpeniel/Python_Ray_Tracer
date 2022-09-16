#!/usr/bin/env python
# this is called a shabang and it is used to make this file executable

# all this boilerplate code is called the shell,
# and it is used to execute main

""" A Pure Python Raytracer by Victor Diaz, 2022,
    based on Arun Ravidran video series
"""
import os.path

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
import importlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('scene', help='Path to the scene file (without the .py extension)')
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDERED_IMG, 'w') as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()
