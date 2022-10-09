# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/permutations-ii/

class Solution:
    def backtracking(self, nums, permutation, result):
        N = len(nums)
        if N == 0:
            result.append(permutation)
            return
        uniques = set()
        for i in range(N):
            if nums[i] not in uniques:
                uniques.add(nums[i])
                self.backtracking(nums[:i]+nums[i+1:], permutation+[nums[i]], result)

        return result
    
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        if N == 1: return [nums]
        return self.backtracking(nums, permutation=[], result=[])