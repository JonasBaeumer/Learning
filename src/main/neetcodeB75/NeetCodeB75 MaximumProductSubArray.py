# Approach we are iteratively going through the row of numbers and multiply them
# If we happen to hit a 0 at some point we will automatically reset the computation to start again
# To prevent information loss when having + and -, we store both value 
# Runtime: O(n)
# Spacetime: O(1)

class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:

        max_so_far, cur_max, cur_min = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            # If current is number is negative this invert our order max is min and vice versa
            if current < 0:
                cur_max, cur_min = cur_min, cur_max
            
            cur_max = max(current, current * cur_max)
            cur_min = min(current, current * cur_min)

            max_so_far = max(max_so_far, cur_max)
            
        return max_so_far
        

# Why this solution fails, we have to be careful with positive and negative numbers and how they switch when being multiplied.
# Suddendly the smallest number multiplied with - can become the biggest and vice versa, therefore in the recursion we are 
# loosing information when this happens since we only look at max not min. Therefore we need to track two solutions at once here. 
# An iterative approach is more suitable.

from functools import cache

class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:

        @cache
        def dfs(start, end):
            # Base case: We have no more elements to multiply
            if start > end:
                return 1
            
            result = max(nums[start] * dfs(1, 0), nums[start] * dfs(start+1, end))

            return result

        answer = -11
        for i in range(len(nums)):
            print(answer)
            answer = max(answer, dfs(i, len(nums)-1))
        return answer
