a = [4 ,5 ,8 ,8 ,8 ,4, 4 ,5 ,2, 3]
b = [4, 5, 8, 2, 8, 4, 3, 5, 2, 3]
n = len(a)
from template import *
# with open('debug.txt', 'w') as f:
if 1:
    seen=set()
    for i in range(1, 100000+1):
    # for j in range(1, 1001):
        val1, val2 = sum(int(k) for k in str(i)), sum(int(k) for k in str(i+1))
        # f.write(f"{val1} {val2} \n")
        seen.add(val2-val1)
        # if val2-val1 != 1:
            # print(val1, val2, i, i+1, sep='\t')
            
            # f.write(f"{val1} {val2} \n")
    print(seen)
    
        
# print(True)