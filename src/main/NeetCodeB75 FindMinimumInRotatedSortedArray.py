# Trivial solution: Simple loop
# Runtime: O(n)
# Spacetime: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_element = 1001

        for i in range(len(nums)):
            if nums[i] < min_element:
                min_element = nums[i]
        
        return min_element
