from functools import cache

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(amount):
            # Base case: We found the right number
            if amount == 0:
                return 0
            # We overshot - no viable solution
            if amount < 0:
                return float("inf")

            coins_used = []
            for number in coins:
                coins_used.append(1 + dfs(amount - number))
            
            return min(coins_used)
        
        amount = dfs(amount)
        return amount if amount != float("inf") else -1
