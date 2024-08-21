# Manuel Ortiz at 2024
# Extracted from: https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePathsHelper(self, m, n, memo):
        if m == 0 and n == 0:
            return 1
        if m<0 or n<0: 
            return 0
        if (memo[m][n] > 0):
            return memo[m][n]
        if (memo[m][n] == 0):
            memo[m][n] = self.uniquePathsHelper(m - 1, n, memo) + self.uniquePathsHelper(m, n - 1, memo)
        
            return memo[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for j in range(n)] for i in range(m)];
        return self.uniquePathsHelper(m-1, n-1, memo)

