# Optimized approach: We can directly pick the highest and the lowest price in one iteration
# Essentially one pointer is for the highest and one pointer for the lowest value we 
# have seen so far
# How can we make sure that we dont update our buying price post setting the selling price?
# We iterate through the array to find the best selling price
# We set first value as buying price, then we loop forward 
# if we find value lower our buying price, this is our new best selling price
# update best_profit
# If we find value higher than best buy_price we update and continue to find new selling prices
# Runtime: O(n)
# Spacetime: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        best_buying_price = 101

        for i in range(len(prices)):
            if (prices[i] < best_buying_price):
                best_buying_price = prices[i]
            else:
                profit = prices[i] - best_buying_price
                if profit > best_profit:
                    best_profit = profit
        
        return best_profit

# Naive approach: Loop and then go from the found solution forward to find best option
# Number of iterations: n - 1 + n - 2 + n - 3 -> n(n+1)/2 -> O(n^2)
# Runtime: O(n^2)
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
