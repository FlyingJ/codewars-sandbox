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

    def flush(self):
        '''
        flush currently cached items
        initializing to empty list
        '''
        self.cached_items = []

    def update(self, value):
        '''
        update cache by simple append of provided value
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

    def get_term(self, term):
        return self(term)

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
        self.fibonacci_sequence = Fibonacci()

    def __call__(self, term):
        return self.fibonacci_sequence(term) * self.fibonacci_sequence(term+1)

    def get_inf(self, target_product):
        '''
        scan Fibonacci product sequence for smallest term equal to, or
        greater than, product
        return index of term satisfying condition and a boolean value
        indicating equality
        '''
        term = 0
        while True:
            fibonacci_product = self(term)
            if fibonacci_product >= target_product:
                return [term, fibonacci_product == target_product]
            term += 1

def get_fib_prod_terms(fibonacci, fibonacci_product, target_product):
    '''
    given:
        - a sequence of type Fibonacci
        - a sequence of type FibonacciProduct
        - a target product
    return
        - the adjacent elements of the Fibonacci sequence whose product has the
        smallest value equal to, or greater than, the target product
        - a boolean value indicating whether the product of the terms is equal
        to the target product
    '''
    term, equality = fibonacci_product.get_inf(target_product)
    return [fibonacci(term), fibonacci(term+1), equality]

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
    print(FIB_PROD.get_inf(5))

#    test.assert_equals(productFib(4895), [55, 89, True])
#    test.assert_equals(productFib(5895), [89, 144, False])
    print(get_fib_prod_terms(FIB, FIB_PROD, 4895) == [55, 89, True])
    print(get_fib_prod_terms(FIB, FIB_PROD, 5895) == [89, 144, False])
