# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                low = mid + 1
            else: 
                high = mid - 1
        
        return low + 1 if nums[low] < target else low
