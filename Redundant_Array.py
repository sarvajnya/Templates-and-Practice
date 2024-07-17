'''
    Author: Sarvajnya Pujari
    Language: Python3
'''

# from sortedlist import *
# import numpy


from collections import Counter
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
dic = defaultdict(int)  # OrderedDict()
seen = set()
int_max = float('inf')  # sys.maxsize
int_min = float('-inf')
# matrix = [[0]*() for _ in range()]
sys.setrecursionlimit(1 << 30)
mod = 1000000007
input = sys.stdin.readline


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


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# def lcm(a, b):
#     return a*b//gcd(a, b)


# def print(*args, end='\n', sep=' '):
#     for i in args:
#         sys.stdout.write(str(i))
#         sys.stdout.write(sep)
#     sys.stdout.write(end)


# def power(a, b, m=mod):
#     '''to return a^b%m in O(logn) time'''
#     res = 1
#     while b:
#         if b & 1:
#             res *= a % m
#         a *= a % m
#         b >>= 1
#     return res % m


def calculate():
    return


def find_min_cost_to_make_elements_equal(A):
    n = len(A)
    unique_elements = set(A)
    min_cost = float('inf')

    for x in unique_elements:
        cost = 0
        left = 0
        right = 0

        current_cost = 0

        while right < n:
            if A[right] != x:
                current_cost += A[right]

            while current_cost > x * (right - left + 1):
                current_cost -= A[left]
                left += 1

            if current_cost == x * (right - left + 1):
                cost = min(cost, x * (right - left + 1))

            right += 1

        min_cost = min(min_cost, cost)


    return min_cost


# Example usage:
if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n = si()
        a = li()
        # ans = 0
        # h = Counter(a)
        # h = sorted(h.items(), reverse=True, key = lambda z:z[1])
        # m = h[0][1]
        # se =  []
        # for i,j in h:
        #     if j == m:
        #         se += [i]
        # res = int_max
        # # print('se', se)
        # for z in se:
        #     c = 0
        #     ans = 0
        #     for i in range(n):
        #         if a[i] != z:
        #             c += 1
        #         else:
        #             ans += (c*z)
        #             c = 0
        #     ans += c*z
        #     res = min(res, ans)
        # if len(set(a)) == 1:
        #     print(0)
        # else:
        #     print(res)
        # Output will be the minimum cost
        print(find_min_cost_to_make_elements_equal(a))
