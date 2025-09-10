# Use a dict to keep store of what we have already seen
# Runtime: O(n)
# Spacetime: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memory_dict = {}

        for index, number in enumerate(nums):
            
            # Check if target-number already key in memory
            if (target - number) in memory_dict:
                return [memory_dict[target - number], index]

            # If not add it
            memory_dict[number] = index

# Naive approach
# Runtime: O(n) x O(n) = O(n^2)
# Spacetime: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index_one, i in enumerate(nums):
            for index_two, j in enumerate(nums):
                if i + j == target and index_one != index_two:
                    return [index_one, index_two]
