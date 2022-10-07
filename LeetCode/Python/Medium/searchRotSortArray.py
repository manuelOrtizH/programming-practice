# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        low = 0
        high = N - 1
        
        #Find the lowest number in the array
        while (low < high):
            mid = (low + high)//2
            
            if (nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid
    
        pivot = low
        low = 0
        high = N - 1
        
        while (low <= high):
            mid = (low + high)//2
            #We have to found the real mid as if the array was sorted
            rotated_mid = (mid + pivot)%N
            if (nums[rotated_mid] == target):
                return rotated_mid
            if(target < nums[rotated_mid]):
                high = mid - 1
            else:
                low = mid + 1
            
        return -1
        