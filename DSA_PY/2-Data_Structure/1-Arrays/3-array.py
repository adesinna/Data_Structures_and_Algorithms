# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twosum(arr: list, tar: int) -> list:
    seen = {}

    for (i, num) in enumerate(arr):
        complement = tar - num

        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i

    return []





