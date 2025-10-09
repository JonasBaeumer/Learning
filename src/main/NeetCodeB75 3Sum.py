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
