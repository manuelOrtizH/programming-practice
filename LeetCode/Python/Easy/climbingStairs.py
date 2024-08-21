# Manuel Ortiz at 2024
# Extracted from: https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairsHelper(self, n, memo):
        if n<0:
            return 0
        
        if memo[n] == 0:
            memo[n] = self.climbStairsHelper(n-1, memo) + self.climbStairsHelper(n-2, memo)
    
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = [0 for x in range(n+1)]
        memo[0] = 1 # Base Case
        return self.climbStairsHelper(n,memo)