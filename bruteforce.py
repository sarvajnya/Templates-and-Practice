from template import *
a=list(range(1,5))
n=len(a)


def calc(a):
    n = len(a)
    tar = n+1

    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1] = pref[i]+a[i]
    f = True
    for i in range(n+1):
        j = 0
        while j < i:
            if (pref[i]-pref[j]) % tar == 0:
                f = False
                break

            j += 1
    return f
for i in permutations(a, n):
    if calc(i):
        print(*i)