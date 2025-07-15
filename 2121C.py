'''
    Author: Sarvajnya Pujari
    Language: PyPy3
'''

def main():
    t = si()
    output_list = []
    for _ in range(t):
        n,m=li() 
        a=[] 
        for i in range(n):
            a+=[li()]
        # print(a)
        x=0 
        for i in range(n):
            for j in range(m):
                x=max(x, a[i][j])


        # r, c = [0]*n, [0]*m 
        # for i in range(n):
        #     for j in range(m):
        #         if a[i][j] == x:
        #             r[i]+=1
        #             c[j]+=1
        # rm, cm=-1, -1 
        # r1,c1=0,0 
        # for i in range(n):
        #     if r[i]>=rm:
        #         rm=r[i]
        #         r1=i
        
        # for j in range(m):
        #     if c[j]>=cm:
        #         if c1 == -1 or c1==r1:
        #             cm=c[j] 
        #             c1=j 
                
        
        # for i in range(n):
        #     for j in range(m):
        #         if i==r1 or j==c1:
        #             a[i][j]-=1
        # # print(r1,c1,r,c,x)
        
        temp = [] 
        rm,cm = [0]*n, [0]*m 
        for i in range(n):
            for j in range(m):
                if a[i][j] == x:
                    temp+=[[i,j]]
                    rm[i]+=1 
                    cm[j]+=1 

        # print(rm,cm,temp)
        r,c=-1,-1 
        ri,ci=-1,-1
        if rm.count(max(rm)) == 1:
            r=rm.index(max(rm))
        if cm.count(max(cm)) == 1:
            c=cm.index(max(cm))

        if r == -1:
            rmax=max(rm)
            for i in range(len(temp)):
                if temp[i][1] == c:
                    continue
                if rm[temp[i][0]] == rmax:
                    r=(temp[i][0])
        
        if c == -1:
            cmax=max(cm)
            for i in range(len(temp)):
                if temp[i][0] == r:
                    continue
                if cm[temp[i][1]] == cmax:
                    c=(temp[i][1])
        
        # if r == -1 and c == -1:
        #     rmax=max(rm)
        #     cmax=max(cm) 
        #     for i in range(len(temp)):
        #         if rm[temp[i][0]] == rmax and r!=c and :
        #             r=(temp[i][0])

                


        for i in range(n):
            for j in range(m):
                if i==r or j==c:
                    a[i][j]-=1
        # for i in range(m):
        #     if r==-1:
        #         ri=i
        #         r=rm[i] 

        #     else:
        #         if rm[i]>r:
        #             ri=
        # print(a,r,c)
        ans=0
        for i in range(n):
            for j in range(m):
                ans=max(ans, a[i][j])
        
        output_list+=[ans]
        
    print('\n'.join(map(str, output_list)).strip())
    pass

'''
res = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))] #transpose of matrix
if f:
    output_list += ['yes']
else:
    output_list += ['no']

'''

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