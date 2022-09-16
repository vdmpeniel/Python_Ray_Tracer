from vector import Vector


class Color(Vector):
    """Stores color as RGB triplets. An alias for vector"""
    @classmethod
    def from_hex(cls, hexcolor='#000000'):
        x = int(hexcolor[1:3], 16) / 256
        y = int(hexcolor[3:5], 16) / 256
        z = int(hexcolor[5:7], 16) / 256
        return cls(x, y, z)
