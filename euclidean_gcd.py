def gcd(a,b):
    while b:        
        a, b = b, a%b
    return a 
def lcm(a,b):
    return a*b//gcd(a,b)
a, b = int(input()), int(input())
print(gcd(a,b))
print(lcm(a,b))