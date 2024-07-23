'''
give max sum in an array <= limit
'''
def find_max_sum(arr, limit):
    n = len(arr)
    current_sum = left = right = 0
    max_sum = float('-inf')

    while right < n:
        current_sum += arr[right]
        while current_sum > limit:
            current_sum -= arr[left]
            left += 1
        max_sum = max(max_sum, current_sum)
        right += 1

    return max_sum
