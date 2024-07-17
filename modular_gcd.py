# cook your dish here
import math
mod = 1000000007
def power(a,power,m):
    res = 1
    while power:
        if power & 1:
            res = ((res%m) * (a%m))%m
        a = (a%m * a%m) % m
        power //= 2
    return res%m

def calc(a,b,n):
    candidate = 1
    if a == b:
        return (power(a, n, mod) + power(b, n, mod))%mod
    i = 1
    num = abs(a-b)
    while i*i <= num:
        if num%i == 0:
            temp = power(a,n,i)+power(b,n,i) 
            if temp % i == 0:
                candidate = max(candidate, i%mod)
            temp = power(a,n,math.ceil(num/i))+power(b,n,math.ceil(num/i)) 
            if temp % math.ceil(num/i) == 0:
                candidate = max(candidate, math.ceil(num/i)%mod)          

        i += 1
    return candidate%mod





t = int(input())
for _ in range(t):
    a,b,n = [int(i) for i in input().split()]
    ans = calc(a,b,n)
    print(ans)