# Optimized approach: Use adjusted version of binary search to solve this
# Essentially: When mid > right we move to right, when mid < right re move to left
# Runtime: O(log n)
# Spacetime: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:

        mid = 0
        left = 0
        right = len(nums)-1

        while (left < right):
            mid = left + (right - left) // 2

            if(nums[mid] > nums[right]):
                left = mid+1
            else:
                right = mid

        return nums[left]

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
