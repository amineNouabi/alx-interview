#!/usr/bin/python3
"""

Minimum Operations Module

"""

import math


def primeFactors(n):
    """ Function to generate prime factors of a number """
    factors = {}
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n = n // i
    if n > 2:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors


def minOperations(n):
    """ Function to calculate the minimum operations """
    factors = primeFactors(n)
    operations = 0
    keys = list(factors.keys())
    print(factors)

    for i in range(len(keys)):
        key = int(keys[i])
        times = factors[keys[i]]
        if i == 0:
            operations += 1
            operations += (key - 1)

            operations += (times - 1) * (1 + key)
        else:
            operations += times * (key + 1)

    return operations


print(minOperations(4))
print(minOperations(12))
