#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
type: Array
site: LeetCode
submission: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1626403412/
"""
class Solution():

    def duplicateArray(self, nums):
        seen = set()
        newArr = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                newArr.append(nums[i])
            seen.add(nums[i])
        nums[:] = newArr
        return len(nums)
    

if __name__ == "__main__":
    sol = Solution()

    input = [1,1,2]
    print(sol.duplicateArray(input))

    input = [0,0,1,1,1,2,2,3,3,4]
    print(sol.duplicateArray(input))