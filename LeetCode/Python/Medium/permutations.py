# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/permutations/

class Solution:
    def backtracking(self, nums, permutation, result):
        N = len(nums)
        if N == 0:
            result.append(permutation)
            return
        for i in range(N):
            self.backtracking(nums[:i]+nums[i+1:], permutation+[nums[i]], result)
        return result
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 1: return [nums]
        return self.backtracking(nums, permutation=[], result=[])