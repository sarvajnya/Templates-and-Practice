def seive(n):
    '''To return list of primes '''
    r = [0]*(n+1)
    r[0] = r[1] = 1
    i = 2
    while i*i <= n:
        if not r[i]:
            j = i*i
            while j <= n:
                r[j] = 1
                j += i
        i += 1
    return r 

n = int(input())
r = (seive(n))
for i in range(len(r)):
    if not r[i]:
        print(i,end=' ')