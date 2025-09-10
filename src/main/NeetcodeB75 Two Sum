# Naive approach
# Runtime: O(n) x O(n) = O(n^2)
# Spacetime: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index_one, i in enumerate(nums):
            for index_two, j in enumerate(nums):
                if i + j == target and index_one != index_two:
                    return [index_one, index_two]
