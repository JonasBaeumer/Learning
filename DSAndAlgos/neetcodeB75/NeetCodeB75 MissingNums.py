# Initial idea: Loop over the list until first value is found that is not in list and return it
# Runtime: O(n^2) since looking up if number in nums is O(n)
# Space: O(1) 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
