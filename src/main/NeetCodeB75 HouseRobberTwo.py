# With this problem similar to our first problem but with a different base case
# We can reuse our solutio from house robber one but with a small caveat
# We have to run with two different cases: We first take the first element but can not include the last
# one / have to stop before or we take the last one but then have to start after the first one
# Runtime: O(n)
# Spacetime: O(n)

from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs(index, stop):
            # Base case: We stepped out of bounds
            if index > stop:
                return 0

            return max(dfs(index + 2, stop) + nums[index], dfs(index + 1, stop))
        
        return max(nums[0], dfs(0, len(nums) - 2), dfs(1, len(nums) - 1))
