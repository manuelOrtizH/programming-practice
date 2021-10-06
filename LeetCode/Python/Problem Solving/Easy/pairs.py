#Manuel Ortiz Hernández
#LeetCode problem solving extracted from: https://leetcode.com/problems/number-of-good-pairs/
from collections import Counter
from typing import List

class Solution:
    def factorial(self, n:int) -> int:
        if n <= 2:
            return n
        else:
            return n*self.factorial(n-1)

    def numIdenticalPairs(self, nums: List[int]) -> int:
        counterOfPairs = 0
        countedNums = Counter(nums)
        for n in countedNums.values():
            if n == 2:
                counterOfPairs+=1
            elif n > 2:
                counterOfPairs += ((self.factorial(n))//(2*self.factorial(n-2)))
        return counterOfPairs

def main():
    sol = Solution()
    nums = [1,2,3,1,1,3]
    print(sol.numIdenticalPairs(nums))

if __name__ == "__main__":
    main()