# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: list[int]) -> int:
        l = len(nums)
        if l == 1: return nums[0]
        if l == 2: return max(nums[0], nums[-1])
        dp = [-1 for x in range(l)]
        return self.robHelper(nums,dp, 0)
    
    def robHelper(self, nums, dp, house):
        if house>=len(nums):
            return 0
        if dp[house] > -1:
            return dp[house]
        
        dp[house] = max(self.robHelper(nums,dp, house+1), nums[house]+self.robHelper(nums,dp, house+2))

        return dp[house]