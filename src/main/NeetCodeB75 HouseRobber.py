# Best solution can change depending on what we will add now so we would have to look at our
# old solution again as it would be invalidated 

# Brute force: Just try all types of combinations of numbers and accept new solution when value is better
# Runtime: 2^n possible solutions since we need to try out all possible combination
# Spacetime O(1) we just need to store best current solution

# Another problem is that we might also be able to jump zig zag so not just all 2 steps starting from
# n-1 and n-2 but we might also do 1 step two step 1 step 

# For the subproblem, for each problem we either have the chance to include n or not
# if we include n, that means we cant look at n-1 (forbidden), so we can only include 
# n-1 vs. taking n
# max(n + n-2, n-1)

# Spacetime: O(n), since we will visit each state once
# Spacetime: O(n), because we keep previous states solutions in cache

from functools import cache

class Solution:
    
    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs(index):
            # Basecase: We overshoot our list
            if index < 0:
                return 0
            best_solution = max(nums[index] + dfs(index-2), dfs(index-1))
            return best_solution
        
        return dfs(len(nums)-1)
