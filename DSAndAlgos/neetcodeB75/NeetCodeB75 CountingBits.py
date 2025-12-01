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
