#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/special-array-i/
problem: https://leetcode.com/problems/special-array-i/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/special-array-i/submissions/1651011908/
"""

class Solution():
  def parityArray(self, s):
    for i in range(len(s) - 1):
        if s[i] % 2 == s[i+1] % 2:
            return False
    return True

if __name__ == "__main__":
    sol = Solution()
    input = [1]
    print(sol.parityArray(input))

    input = [2,1,4]
    print(sol.parityArray(input))


    input = [4,3,1,6]
    print(sol.parityArray(input))
