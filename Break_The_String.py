'''
    Author: Sarvajnya Pujari
    Language: Python3
'''

# from sortedlist import *
# import numpy


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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


def print(*args, end='\n', sep=' '):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)


def power(a, b, m=mod):
    '''to return a^b%m in O(logn) time'''
    res = 1
    while b:
        if b & 1:
            res *= a % m
        a *= a % m
        b >>= 1
    return res % m


def calculate():
    return


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Build the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = ord(data[i]) - ord('a') + 1
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def range_sum(self, l, r):
        # Return the sum of elements in range [l, r)
        l += self.n
        r += self.n
        sum_value = 0
        while l < r:
            if l % 2:
                sum_value += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                sum_value += self.tree[r]
            l //= 2
            r //= 2
        return sum_value


def count_ways_to_split(S):
    n = len(S)
    if n < 3:
        return 0

    # Initialize segment trees for prefix and suffix sums
    prefix_tree = SegmentTree(S)
    suffix_tree = SegmentTree(S[::-1])

    count = 0

    # Iterate through split points
    for i in range(1, n - 1):
        for j in range(i, n):
            prefix_sum = prefix_tree.range_sum(0, i)
            suffix_sum = suffix_tree.range_sum(n - j, n)

            if prefix_sum == suffix_sum:
                P = S[:i]
                R = S[j:]
                Q = P + R

                if P + Q + R == S and P + R == Q:
                    count += 1

    return count


def main():
    import sys
    input = sys.stdin.read().strip().split()
    T = int(input[0])
    results = []

    for i in range(T):
        S = input[i + 1]
        result = count_ways_to_split(S)
        results.append(result)

    for res in results:
        print(res)


if __name__ == "__main__":
    main()
