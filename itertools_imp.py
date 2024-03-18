"""group by"""

import itertools

nums = [1, 1, 2, 2, 3, 1, 2, 3, 4]

for i, j in itertools.groupby(nums):

    print(i, list(j))
