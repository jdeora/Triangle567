import unittest
from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangle(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_equilateral1(self):
        self.assertEqual(classify_triangle([3, 3, 3]), 'Equilateral')

    def testRighttriangleA(self):
        self.assertEqual(classify_triangle([3, 4, 5]), 'Right')

    def testRighttriangleB(self):
        self.assertEqual(classify_triangle([5, 3, 4]), 'Right')

    def testEquilateraltriangles(self):
        self.assertEqual(classify_triangle([1, 1, 1]), 'Equilateral')

    def test_Isosceles1(self):
        self.assertEqual(classify_triangle([2, 3, 3]), 'Isosceles')

    def test_Isosceles2(self):
        self.assertEqual(classify_triangle([2, 3, 2]), 'Isosceles')

    def test_Isosceles3(self):
        self.assertEqual(classify_triangle([3, 2, 2]), 'Isosceles')

    def test_Scalene(self):
        self.assertEqual(classify_triangle([3, 6, 5]), 'Scalene')

    def test_Right(self):
        self.assertEqual(classify_triangle([3, 4, 5]), 'Right')

    def test_Not_a_triangle1(self):
        self.assertEqual(classify_triangle([2, 2, 5]), 'Not_A_Triangle')

    def test_Not_a_triangle2(self):
        self.assertEqual(classify_triangle([2, 5, 2]), 'Not_A_Triangle')

    def test_Not_a_triangle3(self):
        self.assertEqual(classify_triangle([5, 2, 2]), 'Not_A_Triangle')

    def test_Invalid_input1(self):
        self.assertEqual(classify_triangle([-2, 2, 2]), 'Invalid_Input')

    def test_Invalid_input2(self):
        self.assertEqual(classify_triangle([2, -2, 2]), 'Invalid_Input')

    def test_Invalid_input3(self):
        self.assertEqual(classify_triangle([2, 2, -2]), 'Invalid_Input')

    def test_Invalid_input4(self):
        self.assertEqual(classify_triangle([2, 2, 201]), 'Invalid_Input')

    def test_Invalid_input5(self):
        self.assertEqual(classify_triangle([-1, 2, 2]), 'Invalid_Input')

    def test_Invalid_input6(self):
        self.assertEqual(classify_triangle([2, 2, -4]), 'Invalid_Input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
