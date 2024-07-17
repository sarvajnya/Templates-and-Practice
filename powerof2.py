def ispowerof2(n):
    return not(n&(n-1)) and n>0

print(ispowerof2(int(input())))