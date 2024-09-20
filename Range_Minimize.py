'''
    Author: Sarvajnya Pujari
    Language: PyPy3
'''

def main():
    t = si()
    output_list = []
    for _ in range(t):

        n=si() 
        a=li() 
        if n==3:
            output_list+=[0]
        else:
            smallest = nsmallest(3, a)  
            largest = nlargest(3, a)    

            option1 = largest[0] - smallest[2]  
            option2 = largest[2] - smallest[0]  
            option3 = largest[1] - smallest[1]
            res = min(option1, option2, option3)
            # res=max(a)-min(a)
            # temp1=a.copy()
            
            # val1, val2 = nlargest(n, a)[0], nlargest(n, a)[1]
            # a.remove(val1)
            # res = min(res, max(a)-min(a))
            # a.remove(val2)
            # res = min(res, max(a)-min(a))
            # val3, val4 = nsmallest(n, temp1)[0], nsmallest(n, temp1)[1]
            # temp1.remove(val3)
            # res = min(res, max(temp1)-min(temp1))
            # temp1.remove(val4)
            # res = min(res, max(temp1)-min(temp1))
            output_list += [res]
            

    print('\n'.join(map(str, output_list)).strip())
    

def calc():
    pass
    

#Header_Files   
import os
import sys
import math
from io import BytesIO, IOBase

import random
import os

import bisect
import typing
from collections import *
from copy import *
from functools import *
from heapq import *
from itertools import *
from operator import *
from string import *
from typing import *
inf = math.inf

mod = 1e9+7
def input(): return sys.stdin.readline().strip()


BUFSIZE = 4096


#Fast IO using PyRival
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
