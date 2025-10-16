# Naive approach: Run simple for loop
# Runtime: O(n)
# Spacetime: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1
