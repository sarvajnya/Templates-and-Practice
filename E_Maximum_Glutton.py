'''
    Author: Sarvajnya Pujari
    Language: Python3
'''
import os
import sys
import math
from io import BytesIO, IOBase

import random
import os

import bisect
import typing
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import accumulate, combinations, permutations, count, product
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
inf = math.inf

mod = 1e9+7
def input(): return sys.stdin.readline().strip()


BUFSIZE = 4096


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(
                os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(
                b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(
                os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(
                b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdout = IOWrapper(sys.stdout)


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
    a %= m
    while b:
        if b % 2 == 1:
            res = (res*a) % m
        a = (a*a) % m
        b = b // 2
    return res % m


def calc():
    pass


def max_dishes(N, X, Y, A, B):
    # Combine sweetness and saltiness into a list of tuples
    max_dishes_count = 0

    # Iterate over all possible subsets using bitmasking
    for bitmask in range(1 << N):
        current_sweetness = 0
        current_saltiness = 0
        count = 0
        
        for i in range(N):
            if bitmask & (1 << i):
                current_sweetness += A[i]
                current_saltiness += B[i]
                count += 1
        
        if current_sweetness <= X and current_saltiness <= Y:
            max_dishes_count = max(max_dishes_count, count)
    
    return max_dishes_count


if __name__ == '__main__':

    n, x, y = li()
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = li()
    z1 = sorted(zip(a, b))
    z2 = sorted(zip(a, b), key=lambda t: t[1])
    # print(*z)
    res = 0
    ans = 0
    s1 = 0
    s2 = 0
    outs = []
    for i in range(n):
        s1 += z1[i][0]
        s2 += z1[i][1]
        ans += 1
        if s1 > x or s2 > y:
            break

    res = max(res, ans)
    ans = 0
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += z2[i][0]
        s2 += z2[i][1]
        ans += 1
        if s1 > x or s2 > y:
            break
    res = max(res, ans)
    max_dishes_count = 0
    current_sweetness = 0
    current_saltiness = 0
    left = 0
    temp = []
    for i in range(n):
        temp += [abs(z1[i][0]-z1[i][1])]

    z3 = list(zip(temp, a, b))
    z3.sort()
    ans = 0
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += z3[i][1]
        s2 += z3[i][2]
        ans += 1
        if s1 > x or s2 > y:
            break
    res = max(res, ans)

    for right in range(n):
        current_sweetness += z1[right][0]
        current_saltiness += z1[right][1]

        while current_sweetness > x or current_saltiness > y:
            current_sweetness -= z1[left][0]
            current_saltiness -= z1[left][1]
            left += 1

        max_dishes_count = max(max_dishes_count, right - left + 1)

    print(max(res, ans, max_dishes_count, max_dishes(n, x, y, a, b)))
