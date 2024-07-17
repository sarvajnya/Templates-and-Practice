def fun(a, b, m):
    '''to return a^b%m in O(logn) time'''
    res = 1
    while b:
        if b & 1:
            res *= a % m
        a *= a % m
        b >>= 1
    return res % m


a, b, m = [int(i) for i in input().split()]
print(fun(a, b, m))
