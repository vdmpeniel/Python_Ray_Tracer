class Ray:
    """ Half line with normalized direction"""
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
