# Naive idea: We get it as a strong and loop over each field and count the 1s
# Can we also iterate over a binary array?
# Runtime: O(k), k number of bits until last 1
# Spacetime: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = 1
        bit_counter = 0
        while bit <= n:
            print(bit)
            # Here we compare the two bitmasks 
            # & will compare the bits and return true if at least
            # one bit is the same in both numbers 
            # Example: n:1111, bit: 0001 -> First bit found
            # n:1111, bit: 0010 -> second bit found
            # ... 
            if n & bit:
                bit_counter += 1
            # Here we construct our bitmask for the iterations
            # This operations gives us a bitshift such that exactly
            # one bit is 1 while all others are 0
            # This helps us determine which bits in n are 1 (and how many)
            # Example: First round 0001, second 0010, third 0100, fourth 1000
            bit <<= 1
        return bit_counter
