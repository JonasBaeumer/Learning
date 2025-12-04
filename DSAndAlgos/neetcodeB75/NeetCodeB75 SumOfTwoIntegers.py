# Build the plus operator using bits
# Naive approach: we go over the bits of both numbers if they are both 1
# we add vortrag to the next digit, if only one is one we take 1 both 0 we take 0
# According to https://stackoverflow.com/questions/68972991/how-many-bits-are-use-in-bit-manipulation-in-python#:~:text=The%20int%20data%20type%20in,manipulation%20take%20place%20in%20python%3F&text=However%20many%20bits%20the%20numbers%20involved%20require.
# bits have unlimited precision in python and are not fixed size like ints in Java
# which are 32B by default, so how do we know how long we need to iterate?
"""
Algorithm 
Take most right bit of both numbers 
Check next_bit and do the & operator with both numbers
Add next_bit to the number continue
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff      # 32 bits of 1s
        MAX_INT = 0x7fffffff   # Max positive 32-bit int

        # Force a and b into 32-bit range
        a &= MASK
        b &= MASK

        # Just using 32 bit because I know 32bits covers numbers in the million range
        # which is more than enough to keep the -1000 - 1000 intervall
        memory = 0
        number = 0
        for i in range(32):
            bit1 = a & 1 # least significant bit
            bit2 = b & 1 # least significant bit

            sum_bit = bit1 ^ bit2 ^memory
            carry_out = (bit1 & bit2) | (memory & (bit1 ^ bit2)) 

            number |= (sum_bit << i)
            memory = carry_out
            
            a >>= 1
            b >>= 1
            
        # Constrain result to 32 bits
        number &= MASK

        # If sign bit is set, interpret as negative
        if number > MAX_INT:
            return number - (1 << 32)
        return number
