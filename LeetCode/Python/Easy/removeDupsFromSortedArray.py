# Manuel Ortiz at 2023
# Extracted from: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        i = 1
        k = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                nums[k] = nums[i]
                k+=1
            i+=1
        return k