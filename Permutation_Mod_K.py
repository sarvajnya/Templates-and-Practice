'''
    Author: Sarvajnya Pujari
    Language: PyPy3
'''

def main():
    t = si()
    output_list = []
    for _ in range(t):

        n,k = li() 
        l = list(reversed(range(1, n+1)))
        if n == 1:
            output_list += [-1]
            continue
        # if k>=n or k == 1:
        #     for i in range(1, n):
        #         if (i%k) == (l[i-1])%k:
        #             l[i-1],l[i] = l[i], l[i-1] 
        #     output_list += [' '.join(map(str, l)).strip()]
        # else:
        if 1:
            
            
            temp1=[(i)%k for i in range(1, n+1)]
            temp2=[i%k for i in l]
            # print(temp1, temp2, l)
            f=True
            for i in range(n-1):
                j=i
                while j<n:
                    if temp1[i] != temp2[j]:
                        break
                    j+=1
                if j == n:
                    f=False
                    break
                temp2[i], temp2[j] = temp2[j], temp2[i]
                l[i], l[j] = l[j], l[i]
            
            j=n-1
            
            while temp2[j] == temp1[j]:
                if j<0:
                    f=False 
                    break
                j-=1

            if j>=0 and j!=n-1:
                l[-1],l[j] = l[j],l[-1]
                temp2[-1],temp2[j] = temp2[j],temp2[-1]
            for i in range(n):
                if temp1[i] == temp2[i]:
                    f=False 
                    break 
            if f:         
                    
            
        
                output_list += [' '.join(map(str, l)).strip()]
            else:
                output_list += [-1]
                    
            

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
