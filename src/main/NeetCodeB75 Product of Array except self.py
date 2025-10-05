# Problem: I have a nested loop that leads to O(n^2).
# Can I somehow get this down to a single loop or decoupled loops? O(n) or O(2n)
# How do I avoid to do the repeated work??
# Idea: We multiply the array from the ground up! E.g. we have a single number that
# is the multiplication of all numbers in the array! (loop 1)
# Then we go over the array in a new loop and we divide that total number only by nums[i] 
# and that is the results for solutions[i]
# Problem: If I encounter a 0 at any point during the calculation, all other results are 0
# Solution: Remember which indices had 0s, if one 0 all other 0 except this one, if 2 zero everything 0
# Runtime: O(n) + O(n) = O(2n) = O(n)
# Spacetime: O(n) + O(1) = O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solutions = [0] * len(nums)
        product = 1
        zero_locations = set()

        for j in range(len(nums)):
            if (nums[j] != 0):
                product *= nums[j]
            else:
                zero_locations.add(j)

        if len(zero_locations) > 1:
            return solutions

        if len(zero_locations) == 1:
            solutions[next(iter(zero_locations))] = product
            return solutions 
        
        for i in range(len(solutions)):
            if (nums[i] != 0):
                solutions[i] = int(product / nums[i])
            
        return solutions

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
