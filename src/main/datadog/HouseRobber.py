from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs(index):

            # Base case: We have overshot so we cant rob anything 
            if index >= len(nums):
                return 0

            total = 0
            # Decision 1: Rob the current house (so we have to move to index + 2)
            total = max(total, nums[index] + dfs(index + 2))

            # Decision 2: Rob the next house
            total = max(total, dfs(index + 1))

            # Check what decision is best
            return total
        
        return dfs(0)
