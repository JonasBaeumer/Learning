# We are exploring all the possible starting points for each number in the list
# As we can have multiple numbers that are bigger than i, we need to start at each of 
# them and explore which one has the biggest subproblem that we can add
# All numbers smaller are excluded since they are not relevant
# Runtime: O(n^2), numbers in the list, while we say element with memoization, for each element we 
# loop over the list of available elements giving us n iterations per problem
# Spacetime: O(n), recursion stack depth + cache

from functools import cache

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dfs(index):
            # Base case we have reached the end of the list
            if index >= len(nums):
                return 0

            result = 0
            for i in range(index, len(nums)):
                if nums[i] > nums[index]:
                    result = max(result, 1 + dfs(i))
            return result
        
        result = 0
        for index in range(0, len(nums)):
            result = max(result, 1 + dfs(index))
        return result
