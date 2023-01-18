# Manuel Ortiz at 2023
# Extracted from: https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones = 0
        for char in s:
            if char == '0':
                flips += 1
        
        dp = [0] * (len(s)+1)
        dp[0] = flips # cost

        for i in range(1,len(s)+1):
            if s[i-1] == '0':
                flips-=1
            else:
                ones+=1
            dp[i] = min(dp[i-1], ones+flips)
        return dp[len(s)]