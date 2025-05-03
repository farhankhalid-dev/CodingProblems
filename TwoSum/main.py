#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/two-sum/description/
problem: https://leetcode.com/problems/two-sum/description/
type: Easy
site: LeetCode
submission: 
"""

def twoSum(nums, target):
    set = {}
    for i, nums in enumerate(nums):
        compliment = target - nums
        # print(compliment, target, nums, i)
        if compliment in set:
            return [set[compliment], i]
        set[nums] = i
        # print(set)
    return 0
    

if __name__ == "__main__":

    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))

    nums = [3,3]
    target = 6
    print(twoSum(nums, target))