#Manuel Ortiz Hernández
#LeetCode problem solving extracted from: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False for x in range(len(candies))]
        maxKid = 0
        for i in range(len(candies)):
            if candies[i] > maxKid:
                maxKid = candies[i]
        
        for i in range(len(candies)):
            sumCandy = candies[i] + extraCandies
            if sumCandy >= maxKid:
                result[i] = True

        return result

def main():
    sol = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    sol.kidsWithCandies(candies, extraCandies)

if __name__ == "__main__":
    main()