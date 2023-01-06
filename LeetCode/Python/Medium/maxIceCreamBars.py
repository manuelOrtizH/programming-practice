# Manuel Ortiz at 2023
# Extracted from: https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs = sorted(costs)
        i = 0
        while i < len(costs) and costs[i] <= coins:
            coins-= costs[i]
            i+=1
        return i