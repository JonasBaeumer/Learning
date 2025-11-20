from functools import cache

class Solution:
    @cache
    def numDecodings(self, s: str) -> int:

        # Base cases: 
        # - Current string is empty
        # - One character left (only one option)
        # - String leads with 0, not allowed
        if not s or (len(s) <= 1 and s[0] != "0"):
            return 1
        elif s[0] == "0":
            return 0
        
        result = self.numDecodings(s[1:len(s)]) 
        if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
            result += self.numDecodings(s[2:])
        return result

# Runtime: O(n), each substring is computed once due to memoization
# Space: O(n), recursive stack depth + cache storage

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
