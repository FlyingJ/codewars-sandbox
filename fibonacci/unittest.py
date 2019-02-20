#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:58:56 2019

@author: ultra_jason
"""

import unittest

import fibonacci

class TestStringMethods(unittest.TestCase):

    def test_initialize_cache(self):
        positive_test_cases = [[0, 1], [0, 1, 1], ['foo', 'bar', 'baz']]
        for test_case in positive_test_cases:
            self.assertEqual(fibonacci.initialize_cache(test_case), test_case)
        
        negative_test_cases = [0, (0, 1), {'zero': 0}]
        for test_case in negative_test_cases:
            with self.assertRaises(TypeError):
                fibonacci.initialize_cache(test_case)

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
    unittest.main()