#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:58:56 2019

@author: ultra_jason
"""

import unittest

import fibonacci as fb

class TestStringMethods(unittest.TestCase):
    
    def test_Fibonacci_initialize(self):
        fib = fb.Fibonacci()
        self.assertEqual(str(fib), str([0, 1]))
        
    def test_Fibonacci_getitem(self):
        fib = fb.Fibonacci()
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(30), 832040)
        
        answer = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                  987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
                  75025, 121393, 196418, 317811, 514229, 832040]
        self.assertEqual(str(fib), str(answer))
            
#    def test_initialize_cache(self):
#        positive_test_cases = [[0, 1], [0, 1, 1], ['foo', 'bar', 'baz']]
#        for test_case in positive_test_cases:
#            self.assertEqual(fb.initialize_cache(test_case), test_case)
#        
#        negative_test_cases = [0, (0, 1), {'zero': 0}]
#        for test_case in negative_test_cases:
#            with self.assertRaises(TypeError):
#                fb.initialize_cache(test_case)

#    def test_isupper(self):
#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())
#
#    def test_split(self):
#        s = 'hello world'
#        self.assertEqual(s.split(), ['hello', 'world'])
#        # check that s.split fails when the separator is not a string
#        with self.assertRaises(TypeError):
#            s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)