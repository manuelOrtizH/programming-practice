# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        i = 0
        l = len(nums)
        left_sum = 0
        while i < l:
            total_sum -= nums[i]
            if total_sum == left_sum:
                return i
            left_sum += nums[i]
            i+=1
        return -1