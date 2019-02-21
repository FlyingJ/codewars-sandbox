#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:54:16 2019

@author: ultra_jason
"""

class Cache():
    '''
    a class for cache objects
    '''
    def __init__(self, seed=None):
        if seed is None:
            seed = []
        elif not isinstance(seed, list):
            raise TypeError('provided seed for cache is not a list')
        self.cached_items = seed

    def __getitem__(self, index):
        return self.cached_items[index]

    def __repr__(self):
        return str(self.cached_items)

    def update(self, value):
        ''' update cache by simple append of provided value
        '''
        self.cached_items.append(value)

class Fibonacci():
    '''
    a class for fibonacci sequence objects
    '''
    def __init__(self):
        '''
        create a cache object to speed generation of sequence elements
        '''
        self.cache = Cache([0, 1])

    def __call__(self, term):
        try:
            return self.cache[term]
        except IndexError:
            new_value = self(term - 1) + self(term - 2)
            self.cache.update(new_value)
            return new_value
        except TypeError:
            return None

    def __repr__(self):
        return str(self.cache)

class FibonacciProduct():
    '''
    a class for sequences of products of consecutive Fibonacci sequence
    terms
    '''
    def __init__(self):
        '''
        create:
        - cache object to speed generation of sequence elements
        - Fibonacci sequence object
        '''
        self.cache = Cache([])
        self.FIB = Fibonacci()

    def __call__(self, term):
        return self.FIB(term) * self.FIB(term+1)

    def inf_scan(self, target_product):
        '''
        scan Fibonacci product sequence for smallest term equal to, or
        greater than, product
        return index of term satisfying condition and a boolean value
        indicating equality
        '''
        term = 0
        while True:
            FIB_PRODUCT = self(term)
            if FIB_PRODUCT >= target_product:
                return [term, FIB_PRODUCT == target_product]
            term += 1

def productFib(target_product):
    FIB = Fibonacci()
    FIB_PROD = FibonacciProduct()
    term, equality = FIB_PROD.inf_scan(target_product)
    return [FIB(term), FIB(term+1), equality]

if __name__ == '__main__':

    FIB = Fibonacci()
    print(FIB(5))
    print(FIB(0))
    print(FIB(1))
    print(FIB(10))
    print(FIB)
    print(FIB(30))
    print(FIB)

    FIB_PROD = FibonacciProduct()
    print(FIB_PROD(0))
    print(FIB_PROD(1))
    print(FIB_PROD(2))
    print(FIB_PROD.inf_scan(5))

#    test.assert_equals(productFib(4895), [55, 89, True])
#    test.assert_equals(productFib(5895), [89, 144, False])
    print(productFib(4895) == [55, 89, True])
    print(productFib(5895) == [89, 144, False])
