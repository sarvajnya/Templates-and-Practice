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


def rshift(a, n):
    return a[n:]+a[:n]


def calc(a, n, m):
    if n == 1 and m == 1:
        return -1
    b = a.copy()
    if n == 1:
        # for i in range(m//2):
        #     b[0][m-i-1], b[0][i] = b[0][i], b[0][m-i-1]
        # mid = m//2
        # b[0][mid], b[0][mid+1] = b[0][mid+1], b[0][mid]
        try:
            temp = sorted(b[0])
            temp = temp[1:] + temp[:1]
            
            for i in range(m-1):
                if temp[i] == a[0][i]:
                    temp[i], temp[i + 1] = temp[i + 1], temp[i]
            #         b[0][i], b[0][i+1] = b[0][i], b[0][i+1]
            if temp[-1] == a[0][-1]:
                temp[-1], temp[0] = temp[0], temp[-1]
            return [temp]
        except:
            return -1
    for i in range(n):
        b[n-i-1] = a[i]
    if n%2 == 0:        
        return b
    else:
        mid = n//2
        b[mid], b[mid+1] = b[mid+1], b[mid]
        return b
        


if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n, m = li()
        a = [[0] for i in range(n)]
        for i in range(n):
            a[i] = li()
        b = (calc(a, n, m))
        if b != -1:
            for i in b:
                print(*i)
        else:
            print(-1)
