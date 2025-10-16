# Optimized approach
# We check continously which half is sorted and which one is not
# For the sorted one, we then check is our value in between the edges?
# If yes -> Normal binary search, move to right side and repeat
# If algorithm terminates and pointer != target, not present, -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        # Find the sorted half
        while (left <= right):
            mid = (right + left) // 2
            if(target == nums[mid]):
                return mid
            if (nums[left] <= nums[mid]): # Left side sorted!
                if(nums[left] <= target <= nums[mid]): # Value in that half, run BS
                    right = mid - 1
                else:
                    left = mid + 1
            else: # Right side is sorted!
                if(nums[mid] <= target <= nums[right]): # Value in that half, run BS
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# Naive approach: Run simple for loop
# Runtime: O(n)
# Spacetime: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1
