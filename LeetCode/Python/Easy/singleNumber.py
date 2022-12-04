# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq_nums = dict()
        for n in nums:
            freq_nums[n] = freq_nums.get(n,0) + 1
        
        filtered_num = filter(lambda a: freq_nums[a] == 1, freq_nums.keys())
        return next(filtered_num)

sol = Solution()
ans = sol.singleNumber([2,2,1,4,1,3,5,3,5,2])
print(ans)