# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/coin-change/

class Solution:    
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 1:
            return amount
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    memo[i] = min(memo[i], memo[i - coins[j]] + 1)
        # [1,2,5], amount = 11
          #   0  1   2   3   4   5   6   7   8   9  10  11
        # 1  [0  1  12  12  12  12  12  12  12  12  12  12]
        # 2  [0  1   1     12  12  12  12  12  12  12  12]
        
        return memo[amount] if memo[amount] <= amount else -1