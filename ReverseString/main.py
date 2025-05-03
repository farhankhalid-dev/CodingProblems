# !/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-degree-of-a-string/description/
problem: https://leetcode.com/problems/reverse-degree-of-a-string/description/
type: Easy
site: LeetCode
submission: 
"""

def reverseDegree(s):
    total = 0
    for i, ch in enumerate(s):
        rev_alpha_pos = 123 - ord(ch)
        str_pos = i + 1
        total += rev_alpha_pos * str_pos
    return total


if __name__ == "__main__":
    input = "abc"
    print(reverseDegree(input))

    input = "zaza"
    print(reverseDegree(input))
