#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sorting-the-sentence/description/
problem: https://leetcode.com/problems/sorting-the-sentence/description/
type: Sorting
site: LeetCode
submission: https://leetcode.com/problems/sorting-the-sentence/submissions/1629557759/
"""

class Solution():
    def sortSentence(self, s):
        words = s.split()
        print(words[:-1])
        sorted_words = sorted(words, key=lambda x: int(x[-1]))
        result = ' '.join(word[:-1] for word in sorted_words)
        return result

if __name__ == "__main__":
    sol = Solution()

    inp = "is2 sentence4 This1 a3"
    print(sol.sortSentence(inp))
