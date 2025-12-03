# Initial idea: Loop over the list until first value is found that is not in list and return it
# Runtime: O(n^2)
# Space: O(1) 
# Problem lookup for list is not efficient, we can instead turn it into a set for O(1) lookup
# Runtime: O(n) + O(n) -> O(n)
# Space: O(n)
# For the follow up: We can use XOR operation here to determine the number with binary operations
# Runtime: O(n) + O(n) -> O(n)
# Space: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        number = 0
        # We first go through each number that is in that range and add it with XOR
        for i in range(len(nums) + 1):
            number ^= i

        # That we go over the numbers that are actually in nums. Since we have seen all numbers in tha range
        # they cancel out with our existing numbers in nums, expect the one that is missing
        for n in nums:
            number ^= n
        
        return number

# Initial idea: Loop over the list until first value is found that is not in list and return it
# Runtime: O(n^2)
# Space: O(1) 
# Problem lookup for list is not efficient, we can instead turn it into a set for O(1) lookup
# Runtime: O(n) + O(n) -> O(n)
# Space: O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        for i in range(len(nums) + 1):
            if i not in numbers:
                return i
        

# Initial idea: Loop over the list until first value is found that is not in list and return it
# Runtime: O(n^2) since looking up if number in nums is O(n)
# Space: O(1) 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
