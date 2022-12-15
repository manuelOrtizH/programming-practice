# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:

    def lcs(self, s1,s2,i,j, dp):
        if i<0 or j<0:
            return 0

        if dp[i][j] != 0:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.lcs(s1,s2,i-1,j-1, dp)
        else:
            dp[i][j] = max(self.lcs(s1,s2,i-1,j,dp), self.lcs(s1,s2,i,j-1,dp))

        return dp[i][j]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        i = len(text1)
        j = len(text2)
        dp = [[0 for z in range(j)] for x in range(i)]

        return self.lcs(text1, text2, i - 1, j - 1, dp)
