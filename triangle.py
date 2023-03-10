# -- coding: utf-8 --
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""
def classify_triangle(side_lengths):
    """

    Args:
        side_lengths (list of int):lengths of the three sides.
    Returns:
        str:type of triangle formed.
    """
    a,b,c = side_lengths
    if any(side > 200 for side in side_lengths) or any(side <= 0 for side in side_lengths):
        return "Invalid_Input"
    if not all(isinstance(side, int) for side in side_lengths):
        return "Invalid_Input"
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not_A_Triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or a == c or b == c:
        return "Isosceles"
    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        return "Right"
    return "Scalene"
print (classify_triangle([2,3,4]))
