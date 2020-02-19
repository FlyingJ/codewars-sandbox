#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:58:56 2019

@author: ultra_jason
"""

import unittest

import fibonacci as fb

class TestFibonacciMethods(unittest.TestCase):
    
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

    def test_FibonacciProduct_getitem(self):
        fib_prod = fb.FibonacciProduct()
        self.assertEqual(fib_prod(0), 0)
        self.assertEqual(fib_prod(1), 1)
        self.assertEqual(fib_prod(2), 2)

    def test_FibonacciProduct_get_inf(self):
        fib_prod = fb.FibonacciProduct()
        self.assertEqual(fib_prod.get_inf(5), [3, False])
            
    def test_get_fib_prod_terms(self):
        fib = fb.Fibonacci()
        fib_prod = fb.FibonacciProduct()
        self.assertEqual(fb.get_fib_prod_terms(fib, fib_prod, 4895), [55, 89, True])
        self.assertEqual(fb.get_fib_prod_terms(fib, fib_prod, 5895), [89, 144, False])


if __name__ == '__main__':
    unittest.main(verbosity=2)
