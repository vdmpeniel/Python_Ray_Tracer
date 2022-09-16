from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from light import Light
from material import Material
from material import ChequeredMaterial

WIDTH = 1024
HEIGHT = 720
RENDERED_IMG = '2balls.ppm'
CAMERA = Vector(0, 0, -.7)
OBJECTS = [
    # Floor
    Sphere(
        Point(0, 10000.5, 1),
        10000,
        ChequeredMaterial(
            Color.from_hex('#420500'),
            Color.from_hex('#e6b87d'),
            ambient=0.1,
            reflection=0.2
        )
    ),
    # Blue ball
    Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    # Pink ball
    Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980"))),
]
LIGHTS = [
    Light(Point(1.5, -0.1, -1), Color.from_hex('#FFFFFF')),
    Light(Point(-0.75, -2, -2.25), Color.from_hex('#E6E6E6'))
]

