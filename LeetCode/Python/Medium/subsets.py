# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/subsets/

class Solution:
    def backtracking(self,nums,subsets,result):
        if not nums: 
            result.append(subsets)
            return result
        result += [subsets]
        for i in range(len(nums)):
            self.backtracking(nums[i+1:], subsets+[nums[i]], result)
        return result
    
    
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]
        return self.backtracking(sorted(nums), [], [])
        