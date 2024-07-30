'''
    Author: Sarvajnya Pujari
    Language: PyPy3
    created: 30.07.2024 22:25:07 IST
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
from itertools import *
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


if __name__ == '__main__':
    s=ss()
    # z=[]
    # for k,b in groupby(s):
    #     z += [[k,len(list(b))]]
        
    # for i in range(len(z)):
    #     if z[i][0] == 'h' and (i+3) <= len(z) and z[i][1] >= 1:
    #         f=0
    #         for j in range(i+1,i+4):
    #             if j == i+1:
    #                 if z[j][0] == 'e' and z[j][1] >= 1:
    #                     continue 
    #                 else:
    #                     break 
    #             elif j == i+2:
    #                 if z[j][0] == 'l' and z[j][1] >= 2:
    #                     continue
    #                 else:
    #                     break
    #             else:
    #                 if z[j][0] == 'o' and z[j][1] >= 1:
    #                     f=1                         
    #                 else:
    #                     break
    #         if f:
    #             print('YES')
    #             break 
    # if f == 0:
    #     print('NO')
    
    i = 0
    f=False
    while i<len(s):
        if s[i] == 'h':
            j=i+1
            while j<len(s):
                if s[j] == 'e':
                    
                    k=j+1
                    c=0
                    while k<len(s):
                        if s[k] == 'l':
                            c += 1
                        if c == 2:                            
                            l = k+1
                            while l<len(s):
                                if s[l] == 'o':
                                    f=True 
                                    break
                                l += 1 
                            if f:
                                break 
                            k += 1 
                        if f:
                            break                      
                        
                            
                        k += 1 
                    if f:
                        break
                    j += 1           
                            
                    
                j += 1
            if f:
                break
            i += 1
                
        if f:
            break
        i += 1
        
    if f:
        print('YES')
    else:
        print('NO')
    
            
            
    

    # print('\n'.join(map(str, outs)).strip())
