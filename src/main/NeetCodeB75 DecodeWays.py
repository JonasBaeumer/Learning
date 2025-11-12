# Runtime: O(2^n), n number of states because we branch of 2 times per number
# Space: O(n), recursive stack depth

from functools import cache

class Solution:
    @cache
    def numDecodings(self, s: str) -> int:

        # Base case: We have reached the end of the string or current string
        # starts with 0 (which is not allowed)
        if not s:
            return 1
        elif s[0] == "0":
            return 0
        elif (len(s) <= 1 and s[0] != "0"):
            return 1
        
        result = self.numDecodings(s[1:len(s)]) 
        if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
            result += self.numDecodings(s[2:])
        return result
