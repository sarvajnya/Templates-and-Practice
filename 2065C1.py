'''
    Author: Sarvajnya Pujari
    Language: PyPy3
'''

def main():
    t = si()
    output_list = []
    for _ in range(t):
        n, m =li() 
        a=li() 
        b=li()
        f=True
        
        if n == 1:
            output_list += ['YES']
            continue
        # seen=set()
        temp=a.copy() 
        for i in range(n):
            if i == 0:
                temp[i] = min(temp[i], b[0] - temp[i])
                ele = temp[i] 
            else:
                val = b[0] - temp[i]
                if ele <= val and ele <= temp[i]:
                    temp[i] = min(temp[i], b[0] - temp[i]) 
                elif ele<=val:
                    temp[i] = val 
                elif ele > temp[i]:
                    f=False 
                    break
                ele=temp[i]
        # print(temp, f)
        for i in range(n-1):
            if temp[i] > temp[i+1]:
                f=False 
                break 
        
        if f:
            output_list += ['YES']
        else:
            output_list += ['NO']
            
        # for i in range(n-1):
        #     if a[i] > a[i+1]:
                
        #         val = b[0] - a[i]
        #         if val <= a[i+1] and (Wrapper(i) not in seen):
        #             a[i] = val 
        #             seen.add(Wrapper(i))
        #         else:                    
        #             val = b[0]-a[i+1]
        #             if a[i] <= val and (Wrapper(i+1) not in seen):
        #                 a[i+1] = val
        #                 seen.add(Wrapper(i+1))
        #             else:
        #                 f=False 
        #                 break                                             
                        
                 
           
        # if a[n-2] > a[n-1]:                
                
                    
        #         val = b[0] - a[-2]
        #         if val <= a[n-1] and Wrapper(n-2) not in seen:
        #             a[n-2] = val 
        #             seen.add(Wrapper(n-2))
                    
        #         else:                                        
        #             val = b[0]-a[-1]
        #             if a[n-2] <= val and Wrapper(n-1) not in seen:
        #                 a[n-1] = val
        #                 seen.add(Wrapper(n-1))
        #             else:
        #                 f=False 
        # for i in range(n-1):
        #     if a[i] > a[i+1]:
        #         f=False 
        #         break
                  
        # if f:
        #     output_list += ['YES']
        # else:
        #     output_list += ['NO']
        
                
        

    #     pass

    print('\n'.join(map(str, output_list)).strip())
    pass
    

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
