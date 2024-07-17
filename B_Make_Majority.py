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


if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n = si()
        s = ss()
        if n == 1:
            if s[0] == '0':
                print('no')
            else:
                print('yes')
        else:
            i = 0
            while i < len(s)-1:
                if s[i] == '0':
                    j = i+1
                    while j < len(s):
                        if s[j] == '0':
                            j += 1
                        else:
                            break
                    s = s[:i]+'0'+s[j:]
                    i = j
                else:
                    i += 1
            i = 0
            while i < len(s)-1:
                if s[i] == '1':
                    j = i+1
                    while j < len(s):
                        if s[j] == '1':
                            j += 1
                        else:
                            break
                    s = s[:i]+'1'+s[j:]
                    i = j
                else:
                    i += 1
            if len(s) > 1:
                if s[-1] == s[-2]:
                    s = s[:len(s)-1]
            c = Counter(s)
            if c['1'] > c['0']:
                print('yes')
            else:
                print('no')
