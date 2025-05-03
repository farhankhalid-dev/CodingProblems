#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/palindrome-number/
problem: https://leetcode.com/problems/palindrome-number/
type: Palindrome
site: LeetCode
submission: https://leetcode.com/problems/palindrome-number/submissions/1624232598/
"""

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        return original == reversed_num



if __name__ == "__main__":
    sol = Solution()

    input = 121
    print(sol.isPalindrome(input))

    input = -121
    print(sol.isPalindrome(input))

    input = 10
    print(sol.isPalindrome(input))