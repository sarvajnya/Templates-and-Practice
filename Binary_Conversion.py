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

def calc(n,k,s,t):
    c1 = Counter(s)
    c2 = Counter(t)
    l1, l2 = list(c1.keys()), list(c2.keys())
    l1.sort()
    l2.sort()
    if len(c1) != len(c2) or l1 != l2:
        return 'NO'

    for i in c1.keys():
        if c1[i] != c2[i]:
            return 'NO'
    delta=0            
    for i in range(n):
        delta += abs(int(s[i])-int(t[i]))
    shuffle = ceil(delta/2)
    if (shuffle <=k<=n//2) or (shuffle == k):
        return 'YES'
    return 'NO'

    
if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n, k = li()
        s = ss()
        t = ss()
        print(calc(n,k,s,t))
        