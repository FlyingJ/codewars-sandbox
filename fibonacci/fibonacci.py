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

#def initialize_fibonacci_cache():
#    return Cache([0, 1])

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

##def fibonacci_product(n):
##    try:
##        # return cached value
##        return fibonacci_product_cache[n]
##    except IndexError:
#        new_value = fibonacci(n) * fibonacci(n+1)
##        update_cache(fibonacci_product_cache, new_value)
#        return new_value
##    except TypeError:
##        # sequence term identifier must be an integer
##        return None

if __name__ == '__main__':

    FIB = Fibonacci()
    print(FIB(5))
    print(FIB(0))
    print(FIB(1))
    print(FIB(10))
    print(FIB)
    print(FIB(30))
    print(FIB)
#    print(fibonacci(0))
##    print(fibonacci_cache)
#    print(fibonacci(5))
##    print(fibonacci_cache)
#
#    print(fibonacci(10))
#    print(fibonacci(11))
#    print(fibonacci_product(10))
##    print(fibonacci_product_cache)
##    print(fibonacci_cache)
#    test.assert_equals(productFib(4895), [55, 89, True])
#    test.assert_equals(productFib(5895), [89, 144, False])
