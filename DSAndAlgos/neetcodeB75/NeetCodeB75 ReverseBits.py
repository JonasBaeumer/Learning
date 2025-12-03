# Optimal solution, not from me but what is happening here? 
# I think this is trying to shift different parts of the bit row at different times but not sure

class Solution:
    def reverseBits(self, n: int) -> int:
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        return res & 0xFFFFFFFF

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
    # Runtime: O(32) -> O(1) iterate over all 32 bits once
    # Space: O(1) -> just need to store the new number
    def reverseBits(self, n: int) -> int:
        reverse_number = 0
        for i in range(32):
            # Get the least signigicant bit (e.g. most right)
            bit = n & 1
            # Shift the bits to the left to make place to append our new bit at the end
            reverse_number = (reverse_number << 1) | bit
            n >>= 1
        return reverse_number
