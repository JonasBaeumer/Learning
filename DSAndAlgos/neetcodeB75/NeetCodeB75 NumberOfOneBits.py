# Naive idea: We get it as a strong and loop over each field and count the 1s
# Can we also iterate over a binary array?
# Runtime: O(k), k number of bits 
# Spacetime: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = 1
        bit_counter = 0
        while bit <= n:
            if n & bit:
                bit_counter += 1
            bit <<= 1
        return bit_counter
