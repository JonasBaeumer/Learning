# Approach: For each possible solution we explore the space 
# Catch: We cant return -1 once we overshot and the solution is invalid, this is
# because it would get evened out by the 1 step counter on the previous subproblem
# which would make it look like a valid path, thats why we needed to wrap it 
# so that we can make sure we can identify invalid paths
# Runtime: O(n), number of states
# Spacetime: O(n) recursion steck depth + cache

from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(amount):
            # Base case: amount is 0 -> return 0 
            if amount == 0:
                return 0
            # Base case: amount < 0 -> return -1, we overshot
            if amount < 0:
                return float('inf')

            result = float('inf')
            for coin in coins:
                result = min(result, 1+dfs(amount-coin))
            
            return result

        result = dfs(amount)
        return -1 if result == float('inf') else result
