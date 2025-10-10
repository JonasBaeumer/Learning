# Naive approach: Loop and then go from the found solution forward to find best option
# Runtime: O(n log n)?
# Spacetime: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices), 1):
                profit = prices[j] - prices[i]
                if profit > best_profit:
                    best_profit = profit

        return best_profit
