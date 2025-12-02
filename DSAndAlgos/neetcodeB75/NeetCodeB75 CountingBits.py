# Naive approach: For each number in the list do the approach from the previous problem where we deduce the 
# number of bits to get to the solution for each number and store it in the array
# Optimized solution: Can we somehow deduce the number of bits for a number when we have solved the solution
# for a previous number? This would indicate we could use some form of dynamic programming here
# Example: 0001 -> 1, 0010 -> 2 0100 -> 4 1000 -> 8, now 3 would be 0011 (combine previous 
# problems of getting the bits of 1 and 2, since we know that 1,2 have 1 bit each 3 has to have two
# 7 -> 0111 consisting of 4,2,1, could we build the number differently? for example 3 + 3 + 1?
# 3 -> 0011 -> 0011 -> 0001, so how do we find the right subproblems to build this? 
# Idea: Only use all subproblems that consist of exactly one bit because they suffice to build every
# other number in bit representation
# This approach is close but fails for the following reasons:
# DP requires:
#   •	one subproblem, not many
#	•	a deterministic recurrence, not an arbitrary sum
#	•	subproblem ↓ must be strictly smaller
#	•	subproblem must be computable in O(1)
# The decomposition into powers of 2 is not uniquely determined as a function of n, making it unsuitable for DP.
# New DP approach that takes the above requirements into account:
# We can get the next lower number by deducting the lowest 1 bit from the mask
# Example: 14 -> 1110 # 13 -> 1101 and now i & (i-1) = 1100 
# Recursively we could calculate the current bit number by count(i & i-1) + 1

from functools import cache

class Solution:
    def countBits(self, n: int) -> List[int]:

        num_bits = []
        # Example n = 4
        print(n) # 0100 -> 4
        print(n-1) # 0011 -> 3
        print(n & n-1) # Overlap is 0 so 0000 + 1 means 1 bit

        @cache
        # This one returns the number of bits for a given number
        def dfs(n):
            # Base case number 0
            if n == 0:
                return 0
            return dfs(n & n-1) + 1

        for number in range(n+1):
            num_bits.append(dfs(number))
        return num_bits

# Runtime: O(n) * O(k) number of bits
# Space: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []

        for number in range(0, n+1):
            bit = 1
            bit_counter = 0
            while bit <= n:
                if number & bit:
                    bit_counter +=1
                bit <<= 1
            bits.append(bit_counter)
        return bits
