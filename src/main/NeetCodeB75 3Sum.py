# Optimized approach: We are sorting our array and then using two pointer to move forward
# Then we can move from the start of the array up
# For every item in the array: we then put our left pointer at the next element and our right pointer at the right
# We let the pointers move towards each other and the pointers have the purpose of finding 
# the two values that together equal 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        tripplets = []
        stored_tripplets = set()
        
        for i in range(len(sorted_nums)):
            left = i+1
            right = len(nums)-1

            while(left < right):
                sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if(sum == 0):
                    if (tuple(sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])) not in stored_tripplets):
                        tripplets.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                        stored_tripplets.add(tuple(sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])))
                    left += 1
                    right -= 1
                elif (sum < 0):
                    left += 1
                else:
                    right -= 1

        return tripplets

# Naive approach: Tripple nested loop with three pointers to capture all variations,
# use hashset to check for triplets that are already included in the list to normalize
# tripplet combinations
# Runtime: O(n^3) BAD
# Spacetime: O(t) (number of valid tripplets)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        used_tripplets = set()
        tripplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    tripplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if (nums[i] + nums[j] + nums[k] == 0) and (tripplet not in used_tripplets) and len({i, j, k}) == 3:
                        used_tripplets.add(tripplet)
                        tripplets.append(tripplet)

        return tripplets
