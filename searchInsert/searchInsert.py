#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/search-insert-position/
problem: https://leetcode.com/problems/search-insert-position/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/search-insert-position/submissions/1642326665/
"""

class Solution():
  def searchInsert(self, nums, target):
    lengthArr = len(nums)
    for i in range(lengthArr):
      if target == nums[i]:
        return i
      elif target < nums[i]:
        return i
      elif i == lengthArr -1:
        return i+1



if __name__ == "__main__":
    sol = Solution()

    nums = [1,3,5,6]
    target = 5
    print(sol.searchInsert(nums, target))

    nums = [1,3,5,6]
    target = 2
    print(sol.searchInsert(nums, target))

    nums = [1,3,5,6]
    target = 7
    print(sol.searchInsert(nums, target))

    nums = [1]
    target = 1
    print(sol.searchInsert(nums, target))
