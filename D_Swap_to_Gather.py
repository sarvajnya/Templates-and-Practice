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
    # t = si()
    # output_list = []
    # for _ in range(t):

    #     pass

    # print('\n'.join(map(str, output_list)).strip())
    n = si()
    s = ss()
    if s.count('1') == 1:
        print(0)
    else:

        o = set()
        z = set()
        for i in range(n):
            if s[i] == '1':
                o.add(i)
            else:
                z.add(i)

        i = 0
        temp1, temp2 = list(o), list(z)
        reach = temp1[len(temp1)//2]
        # print(temp1, temp2)
        # print(reach)
        res = 0
        while i < len(o):
            if temp1[i] < reach:
                ind = bisect.bisect_right(temp2, reach) - 1

                res += abs(temp1[i]-temp2[ind])
                
                z.remove(temp2[ind])
                print(temp1[i], temp2[ind])
                i += 1
            if temp1[i] > reach:

                # print(temp2, reach)
                ind = bisect.bisect_left(temp2, reach)

                res += abs(temp1[i]-temp2[ind])
                print(temp1[i], temp2[ind])
                i += 1
                z.remove(temp2[ind])
                

            else:
                i += 1
            temp1, temp2 = list(o), list(z)
        print(res)


def calc():
    pass


# Header_Files


inf = math.inf

mod = 1e9+7
def input(): return sys.stdin.readline().strip()


BUFSIZE = 4096


# Fast IO using PyRival

RANDOM = random.randrange(2**62)


def Wrapper(x):
    return x ^ RANDOM


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


def print(*args, end='\n', sep=''):
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
