'''O(m^3 logn)
Matrix should be square'''

def fun(mat, power):
    n = len(mat)

    '''Identity matrix'''
    iden = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                iden[i][j] = 1
            else:
                iden[i][j] = 0
    while power:        
            if power & 1:            
                temp = [[0]*n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            temp[i][j] += iden[i][k]*mat[k][j]
                
                for i in range(n):
                    for j in range(n):
                        iden[i][j] = temp[i][j]
        
            temp = [[0]*n for _ in range(n)]     
            for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            temp[i][j] += mat[i][k]*mat[k][j]
                
            for i in range(n):
                for j in range(n):
                    mat[i][j] = temp[i][j]
            power //= 2

    return iden







n, power = [int(i) for i in input().split()]
a = [[None]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
res = fun(a, power)
print(res)