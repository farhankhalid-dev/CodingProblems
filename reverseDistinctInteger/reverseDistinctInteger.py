#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/?envType=problem-list-v2&envId=hash-table
problem: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/?envType=problem-list-v2&envId=hash-table
type: Medium
site: LeetCode
submission: xyz
"""

class Solution():
  def reverseDistinctInteger(self, nums):
    distinct = set(nums)
        for num in nums:
            reversed_num = int(str(num)[::-1])
            distinct.add(reversed_num)
            
        return len(distinct)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,13,10,12,31]
    print(sol.reverseDistinctInteger(nums))

    nums = [2,2,2]
    print(sol.reverseDistinctInteger(nums))
