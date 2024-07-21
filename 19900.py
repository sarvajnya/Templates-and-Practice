'''
    Author: Sarvajnya Pujari
    Language: Python3
'''

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
int_max = float('inf')  # sys.maxsize
int_min = float('-inf')
# sys.setrecursionlimit(1 << 30)
input = sys.stdin.readline
mod = 1000000007


def print(*args, end='\n', sep=' '):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)


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


def power(a, b, m=mod):
    '''to return a^b%m in O(logn) time'''
    res = 1
    a = a % m
    while b:
        if b & 1:
            res = (res*a) % m
        a = (a*a) % m
        b >>= 1
    return res % m


def find_factors(n):
    '''To find all factors of n except itself'''
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors


def calc(n, a):
    if n == 1:
        return 1
    m = max(a)
    if a.count(m) % 2 != 0:
        return 1
    rem = (n-a.count(m))
    if rem == 0:
        return 0
    c = Counter(a)
    for k, v in c.items():
        if v % 2 != 0:
            return 1
    # a2 = []
    # for i in a:
    #     if i != m:
    #         a2 += [i]
    # print(a2)
    # if a2.count(max(a2)) % 2 != 0:
    #     return 1
    return 0


if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n = si()
        a = li()
        ans = calc(n, a)
        if ans == 1:
            print("YES")
        else:
            print("NO")
