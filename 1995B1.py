'''
    Author: Sarvajnya Pujari
    Language: Python3
'''

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
int_max = float('inf')  # sys.maxsize
int_min = float('-inf')
# sys.setrecursionlimit(1 << 30)
input = sys.stdin.readline
mod = 1000000007


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
    a = a % m
    while b:
        if b & 1:
            res = (res*a) % m
        a = (a*a) % m
        b >>= 1
    return res % m


def find_factors(n):
    '''To find all factors of n except itself'''
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.sort()
    return factors


def calc():
    pass


def find_groups_with_max_diff_1(lst):
    n = len(lst)
    groups = []

    for i in range(n):
        current_group = [lst[i]]
        for j in range(i + 1, n):
            if max(current_group) - min(current_group) <= 1:
                current_group.append(lst[j])
            else:
                break
        if max(current_group) - min(current_group) <= 1:
            groups.append(tuple(current_group))

    return groups


def find_max_sum(arr, limit):
    n = len(arr)
    current_sum = left = right = 0
    max_sum = float('-inf')

    while right < n:
        current_sum += arr[right]
        while current_sum > limit:
            current_sum -= arr[left]
            left += 1
        max_sum = max(max_sum, current_sum)
        right += 1

    return max_sum


if __name__ == '__main__':
    t = si()
    for _ in range(t):
        n, m = li()
        a = li()
        # a.sort(reverse=True)
        c = Counter(a)
        c = dict(sorted(c.items(), reverse=True))
        res = []
        temp = list(c.keys())
        j = 0
        # if m >= c[base]*base:
        #     ans += c[base]*base
        #     m -= c[base]*base
        # for i in range(len(temp)-1):
        #     if abs(base-temp[i+1]) > 1:
        #         break
        #     if m >= c[temp[i+1]]*temp[i+1]:
        #         ans += c[temp[i+1]]*temp[i+1]
        #         m -= c[temp[i+1]]*temp[i+1]
        i = 1
        inter = [temp[j]]*c[temp[j]]
        while i < len(temp):
            if temp[j]-temp[i] > 1:
                res += [inter]
                inter = []
                j += 1
                if j == i:
                    i += 1
                inter += [temp[j]]*c[temp[j]]

            else:
                inter += [temp[i]]*c[temp[i]]
                i += 1
        res += [inter]
        # print(res)
        dict2 = defaultdict(int)
        ans = 0
        # print(res)
        for i in res:
            j = 0
            val = find_max_sum(i, m)
            ans = max(ans, val)
        print(ans)

        # for key in c.items():
