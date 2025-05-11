#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/roman-to-integer/description/
problem: https://leetcode.com/problems/roman-to-integer/description/
type: Conversion
site: LeetCode
submission: https://leetcode.com/problems/roman-to-integer/submissions/1631261087/
"""

class Solution():
  def romanToInteger(self, input):
    my_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
    sum = 0
    for i in range(len(input)):
      if i + 1 < len(input) and my_dict[input[i]] < my_dict[input[i + 1]]:
        sum -= my_dict[input[i]]
      else:
        sum += my_dict[input[i]]
    return sum

  


if __name__ == "__main__":
    sol = Solution()

    input = "III"
    print(sol.romanToInteger(input))

    input = "LVIII"
    print(sol.romanToInteger(input))

    input = "MCMXCIV"
    print(sol.romanToInteger(input))

