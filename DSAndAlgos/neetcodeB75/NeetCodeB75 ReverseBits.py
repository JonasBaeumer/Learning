# Input: 21 -> 00000000000000000000000000010101
# Max - Input: 11111111111111111111111111101010

# Naive approach: Use bitshift in some from / capacity to move the bits around 
# 1100 -> 0011
# 001010 -> 010100 (reverse like a string) abc -> cba
# Idea: We treat is as a two pointer solution where we go through the initial number from the right
# and then add the number at the right side continously this way the bit will build up in reverse order
# Example: 1110010 -> 0100111

class Solution:

    """
    Take most right bit of the original number
    if bit 1 add 1 else add 0 to the most right position of new_number
    shift bits of the original number to the right by one position
    """
    def reverseBits(self, n: int) -> int:
        reverse_number = 0
        for i in range(32):
            # Get the least signigicant bit (e.g. most right)
            bit = n & 1
            # Shift the bits to the left to make place to append our new bit at the end
            reverse_number = (reverse_number << 1) | bit
            n >>= 1
        return reverse_number
