import unittest
from triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_equilateral1(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_Isoceles1(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')

    def test_Isoceles2(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles')

    def test_Isoceles3(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isoceles')

    def test_Scalene(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene')

    def test_Right(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def test_Not_a_triangle1(self):
        self.assertEqual(classifyTriangle(2, 2, 5), 'NotATriangle')

    def test_Not_a_triangle2(self):
        self.assertEqual(classifyTriangle(2, 5, 2), 'NotATriangle')

    def test_Not_a_triangle3(self):
        self.assertEqual(classifyTriangle(5, 2, 2), 'NotATriangle')

    def test_Invalid_input1(self):
        self.assertEqual(classifyTriangle(-2, 2, 2), 'InvalidInput')

    def test_Invalid_input2(self):
        self.assertEqual(classifyTriangle(2, -2, 2), 'InvalidInput')

    def test_Invalid_input3(self):
        self.assertEqual(classifyTriangle(2, 2, -2), 'InvalidInput')

    def test_Invalid_input4(self):
        self.assertEqual(classifyTriangle(2, 2, 201), 'InvalidInput')

    def test_Invalid_input5(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'InvalidInput')

    def test_Invalid_input6(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'InvalidInput')

    def test_Invalid_input7(self):
        self.assertEqual(classifyTriangle(2, 2, 5), 'InvalidInput')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
