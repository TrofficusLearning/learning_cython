from __future__ import print_function
from timeit import timeit

def pysum(n):
    sum = i = 0
    while i < n:
        sum += i
        i += 1
    return sum

print(f"Pure python version: {timeit('pysum(100)', 'from __main__ import pysum')}")
print(f"Cython version: {timeit('sum(100)', 'from cython_hello_world import sum')}")
