def factors(n):
    r = [0]*(n+1)
    r[0] = r[1] = 1
    i = 2
    while i<=n:
        if not r[i]:
            j = i
            while j<=n:
                if not r[j]:
                    r[j] = i 
                j += i 
        i += 1

    res = []
    while n>1:
        res += [r[n]]
        n//=r[n]

    return res

print(factors(int(input())))
