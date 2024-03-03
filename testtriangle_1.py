# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle_1 import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')
        
    def testNotATriangleTriangles(self): 
        self.assertEqual(classify_triangle(1,2,3),'NotATriangle','1,2,3 is not a triangle')
        
    def testScaleneTriangles(self): 
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 should be Scalene')    
       
    def testIsoscelesTriangles(self): 
        self.assertEqual(classify_triangle(3,3,4),'Isosceles','3,3,4 should be Isosceles')
       
    def testInvalidInput(self): 
        self.assertEqual(classify_triangle(205,8,3),'InvalidInput','205,8,3 is not a triangle ') 
   
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
