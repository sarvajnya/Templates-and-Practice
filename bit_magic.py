'''Print powers of 2'''
def print_pow(n):
    i=1
    while i<=n:
        print(i)
        i<<=1

'''check if ith bit is set
starts from 0'''
def isset(i, n):
    return bool(1<<i & n)


# n = int(input())
# for i in range(2**n):
#     print_pow(i)
print(isset(0,1))



