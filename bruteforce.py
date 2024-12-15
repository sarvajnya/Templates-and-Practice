a = [4 ,5 ,8 ,8 ,8 ,4, 4 ,5 ,2, 3]
b = [4, 5, 8, 2, 8, 4, 3, 5, 2, 3]
n = len(a)
from template import *
for i in range(n):
    d = Counter(b[:i+1])
    if max(d.values()) > d[a[i]]:
        print(False, i)
        exit(0) 
print(True)