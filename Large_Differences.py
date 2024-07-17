'''
    Author: Sarvajnya Pujari
    Language: Python3
'''

# from sortedlist import *
# import numpy


from math import *
from collections import *
from itertools import *
import sys
import os
import io
import string
from bisect import *
from heapq import *
from functools import *
dic = defaultdict(int)  # OrderedDict()
seen = set()
int_max = float('inf')  # sys.maxsize
int_min = float('-inf')
# matrix = [[0]*() for _ in range()]
sys.setrecursionlimit(1 << 30)
mod = 1000000007
input = sys.stdin.readline


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


def print(*args, end='\n', sep=' '):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)


def power(a, b, m=mod):
    '''to return a^b%m in O(logn) time'''
    res = 1
    while b:
        if b & 1:
            res *= a % m
        a *= a % m
        b >>= 1
    return res % m


if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n, k = li()
        a = li()
        ans = 0
        min_ind = 0
        if n == 2:
            print(abs(a[0]-a[1]))
            continue
        min_ind = n//2
        val = 1
        temp = abs(a[min_ind-1]-a[min_ind])+abs(a[min_ind]-a[min_ind+1])
        while val <= k:
            temp = max(temp, abs(a[(min_ind)-1] - val) +
                       abs(a[(min_ind)+1] - val))
            val += 1

        for i in range(n-1):
            if i == (min_ind-1) or i == min_ind:
                continue
            ans += abs(a[i]-a[i+1])
        print(ans+temp)
