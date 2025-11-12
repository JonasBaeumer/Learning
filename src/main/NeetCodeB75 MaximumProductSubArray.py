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
