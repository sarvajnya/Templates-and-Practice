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
    t = si()
    output_list = []
    for _ in range(t):

            a, b = li()
            xk, yk = li()
            xq, yq = li()
            temp1 = ([[xq, yq], [xk, yk]])
            
        
            ans = 0        
            v1=m1-a
            v2=m2-a 
                    
            v3=m1+a 
            v4=m2+a
                    
            v5=m1+a
            v6=m2-a 
                    
            v7=m1-a 
            v8=m2+a
                    
            v9 = m1-b
            v10 = m2-b

            v11 = m1+b
            v12 = m2+b

            v13 = m1+b
            v14 = m2-b

            v15 = m1-b
            v16 = m2+b
            temp2 = [[v1,v2], [v3,v4], [v5,v6],[v7,v8],[v9,v10],[v11,v12],[v13,v14],[v15,v16]] 
                    
            if(temp1[0] in temp2 and temp1[1] in temp2):                        
                ans += 1
            output_list += [ans]

    print('\n'.join(map(str, output_list)).strip())


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
