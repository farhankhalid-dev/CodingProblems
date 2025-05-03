#!/usr/bin/env python3

"""
source: https://neetcode.io/problems/duplicate-integer
problem: https://neetcode.io/problems/duplicate-integer
type: Arrays
site: NeetCode
submission: https://leetcode.com/problems/contains-duplicate/submissions/1624443410/ 
"""
class Solution:
    def isDuplicate(self, x):
        seen = set()
        for val in x:
            if val in seen:
                return True
            seen.add(val)
        return False


if __name__ == "__main__":
    sol = Solution()

    input = [1,2,3,1]
    print(sol.isDuplicate(input))

    input = [1, 2, 3, 4]
    print(sol.isDuplicate(input))

    input = [1,1,1,3,3,4,3,2,4,2]
    print(sol.isDuplicate(input))

    input = [3,3]
    print(sol.isDuplicate(input))

