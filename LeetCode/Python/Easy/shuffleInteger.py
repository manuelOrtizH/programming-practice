#Manuel Ortiz Hernández
#LeetCode problem solving extracted from: https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:        
        i = 0
        result = []
        while i<n: 
            result.insert(i*2, nums[i])
            i+=1
        y_pos = (i-1)
        while i<len(nums):
            half = y_pos - (i-n)
            result.insert(i-half, nums[i])
            i+=1
        return result
 

def main():
    sol = Solution()
    nums = [2,5,1,3,4,7]
    n = 3
    print(sol.shuffle(nums, n))

if __name__ == "__main__":
    main()
