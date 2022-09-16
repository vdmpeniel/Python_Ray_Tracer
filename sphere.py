from math import sqrt


class Sphere:
    """Sphere has radius, center, and material"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        sphere_to_ray = ray.origin - self.center
        # a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            distance = (-b - sqrt(discriminant)) / 2
            if distance > 0:
                return distance
        return None


