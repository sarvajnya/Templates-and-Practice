'''
    Author: Sarvajnya Pujari
    Language: Python3
'''

# from sortedlist import *
# import numpy


# from math import *
# from collections import *
# from itertools import *
# import sys
# import os
# import io
# import string
# from bisect import *
# from heapq import *
# from functools import *
# dic = defaultdict(int)  # OrderedDict()
# seen = set()
# int_max = float('inf')  # sys.maxsize
# int_min = float('-inf')
# # matrix = [[0]*() for _ in range()]
# sys.setrecursionlimit(1 << 30)
# mod = 1000000007
# input = sys.stdin.readline


def si(types=None):
    if not types:
        return int(input().strip())
    return int(types)


def sf(types=None):
    if not types:
        return float(input().strip())
    return float(types)


def ss(types=None):
    if not types:
        return input().strip()
    return str(types)


def li(types=None):
    if not types:
        return list(map(int, input().strip().split()))
    return list(map(int, str(types)))


def mi(types):
    return map(int, str(types))


def ms(types):
    return map(str, str(types))


def mf(types):
    return map(float, str(types))


def lf(types=None):
    if not types:
        return list(map(float, input().strip().split()))
    return list(map(float, str(types)))


def ls(types=None):
    if not types:
        return list(input().strip().split())
    return list(map(str, str(types)))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


# def print(*args, end='\n', sep=' '):
#     for i in args:
#         sys.stdout.write(str(i))
#         sys.stdout.write(sep)
#     sys.stdout.write(end)


# def power(a, b, m=mod):
#     '''to return a^b%m in O(logn) time'''
#     res = 1
#     while b:
#         if b & 1:
#             res *= a % m
#         a *= a % m
#         b >>= 1
#     return res % m


def fins(n):
    # array = [-1]*n
    # array[0]=1
    # for i in range(2, n+1):
         
    #     j = i
    #     while j<=n:
    #         if array[j-1] == -1:
    #             array[j-1] = j
    #         j += i
    # return array
    return list(range(1, n+1))
    

if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n = si()
        l=fins(n)
        print(*l)
        
