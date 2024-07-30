n = 0
arr = []

# created: 28.07.2024 20:16:44 IST

'''
if pref[i]-i == pref[j]-j then subarray is found
'''
pref = [0]*(n+1)
for i in range(n):
    pref[i+1] = pref[i]+arr[i]
    max_len = -1
    index_map = {}
    for i in range(n+1):
        current_value = pref[i] - i

        if current_value in index_map:
            max_len = max(max_len, i - index_map[current_value])
        else:
            index_map[current_value] = i
