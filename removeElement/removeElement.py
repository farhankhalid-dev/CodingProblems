#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/remove-element/description/
problem: https://leetcode.com/problems/remove-element/description/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/remove-element/submissions/1640541636/
"""

class Solution():
  def removeElement(self, input, target):
    k = 0 
    for i in range(len(input)):
      if input[i] != target:
          input[k] = input[i]
          k += 1
    return k

if __name__ == "__main__":
    sol = Solution()
    input = [3,2,2,3]
    target = 3
    print(sol.removeElement(input, target))

    input = [0,1,2,2,3,0,4,2]
    target = 2
    print(sol.removeElement(input, target))