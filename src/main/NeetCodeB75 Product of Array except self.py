# Naive approach: Go over the array N times and just skip position i
# Runtime: O(n) x O(n) = O(n^2)
# Spacetime: O(n) + O(1) = O(n)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solutions = [0] * len(nums)
        product = 1

        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j:
                    product *= nums[i]

            solutions[j] = product
            product = 1
