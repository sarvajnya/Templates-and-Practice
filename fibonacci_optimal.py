"""Get nth fibonacci number in log(n)
OR
fibonacci series
OR
No of binary strings of length n not having consecutive 1s -> (n+2)th fib number
Tip: AFTER 300 fib last 2 digits repeat"""


def fun(power):
    mat = [[0, 1], [1, 1]]

    """Identity matrix"""
    iden = [[1, 0], [0, 1]]

    a = [[0, 1]]
    while power:
        if power & 1:
            temp = [[0] * 2 for _ in range(2)]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        temp[i][j] += iden[i][k] * mat[k][j]

            for i in range(2):
                for j in range(2):
                    iden[i][j] = temp[i][j]

        temp = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    temp[i][j] += mat[i][k] * mat[k][j]

        for i in range(2):
            for j in range(2):
                mat[i][j] = temp[i][j]
        power //= 2

    ans = iden[1][0]
    return ans


n = int(input())
print(0, end=" ")
for i in range(1, n + 1):
    ans = fun(i)
    print(ans, end=" ")
