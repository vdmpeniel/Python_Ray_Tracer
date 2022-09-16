import unittest
from vector import Vector


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)
        
    def test_magnitude(self):
        self.assertEqual(10.392304845413264, self.v2.magnitude())
       
    def test_addition(self):
        result = self.v1 + self.v2
        self.assertEqual(4, getattr(result, 'x'))

    def test_multiplication(self):
        result = self.v2 * 2
        self.assertEqual(12, getattr(result, 'y'))

    def test_division(self):
        result = self.v2 / 2
        self.assertEqual(3, getattr(result, 'y'))


if __name__ == 'main':
    unittest.main()
