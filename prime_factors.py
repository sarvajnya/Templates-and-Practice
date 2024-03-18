'''O(sqrt(N))'''
def calc(n):
    for i in range(2, int(n**0.5)+1):
        count = 0
        while n%i == 0:
            n//=i
            count += 1
        if count:
            print(f'{i}^{count}', end = ' ')
    if n>1:
        print(f'{n}^{1}')

calc(int(input()))