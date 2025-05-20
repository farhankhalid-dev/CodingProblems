#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/determine-if-string-halves-are-alike/
problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1639579536/?envType=problem-list-v2&envId=string
"""

class Solution():
    def halfStringsAlike(self, s):
        vowels = set('aeiouAEIOU')
        half = len(s) // 2
        leftArr = s[:half]
        rightArr = s[half:]
        
        left = sum(1 for ch in leftArr if ch in vowels)
        right = sum(1 for ch in rightArr if ch in vowels)

        return left == right

if __name__ == "__main__":
    sol = Solution()
    input_str = "book"
    print(sol.halfStringsAlike(input_str))
