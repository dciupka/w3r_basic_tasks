def find_max(nums):
    max_num = float('-inf')
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def find_min(nums):
    min_num = float("inf")
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


numbers = [444, 2, 3, 4, 20000, 2, 44]
print(find_max(numbers))
print(find_min(numbers))

import sys

least_value = sys.maxsize
print(least_value)
