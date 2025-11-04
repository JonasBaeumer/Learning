# Approach: We are exploring our solution space with two possible steps, for each level
# we can either step down one stair or two stairs at once.
# Runtime: O(2^n)
# Spacetime: O(n)
# For each step we branch two time hence O(2^n)
# Why is spacetime O(n) -> The callstack will only cover on branch of the recursion tree at a time
# not the whole tree and it has O(n) depth
# Problem: Here we have a lot of double computation that we do that is not necessary
# for example n=3 -> n(3-1), n(3-2) appear in different sides of the tree so it is the same subtree!

class Solution:
    
    def climbStairs(self, n: int) -> int:
        # Base case: We overstepped (e.g. this path was not valid and must be stopped)
        if n < 0:
            return 0
        # Base case: I cant walk anymore steps since we have reached the end
        if n == 0:
            return 1
        # Now we explore the possibilities when going down either a single step or two steps
        one_step = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return one_step 
