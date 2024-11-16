'''
    Author: Sarvajnya Pujari
    Language: PyPy3
'''

from typing import *
from string import *
from operator import *
from itertools import *
from heapq import *
from functools import *
from copy import *
from collections import *
import typing
import bisect
import random
from io import BytesIO, IOBase
import math
import sys
import os


def main():
    n, k = li()
    s = ss()
    a1 = []
    a2 = []
    c1 = 0
    c2 = 0
    for i in range(n):
        if s[i] == '1':
            c1 += 1
            if c2:
                a2 += [c2]
                c2 = 0
        else:
            c2 += 1
            if c1:
                a1 += [c1]
                c1 = 0
    if c1:
        a1 += [c1]
    if c2:
        a2 += [c2]
    k -= 1
    if s[0] == '0':
        l = sum(a1[:k]+a2[:k])
        ans = s[:l]
        j=0
        if k<len(a1):
            j += a1[k]
        if k < len(a2):
            j += a2[k]
        ans += ''.join(reversed(s[l:l+j]))
        ans += s[l+j:]
        print(ans)
    else:
        l = sum(a1[:k-1]+a2[:k-1])
        
        ans = s[:l+1]
        l=a1[k-1]
        j=0
        if k<len(a1):
            j += a1[k]
        if k-1 < len(a2):
            j += a2[k-1]
        ans += ''.join(reversed(s[l:l+j]))
        ans += s[l+j:]
        print(ans)


def calc():
    pass


# Header_Files


inf = math.inf

mod = 1e9+7
def input(): return sys.stdin.readline().strip()


BUFSIZE = 4096


# Fast IO using PyRival
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


if __name__ == '__main__':
    main()
