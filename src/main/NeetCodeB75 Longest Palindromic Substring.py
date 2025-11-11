# New approach, we can consider each string to be the middle of the palindrome
# and then run outwards in both direction, must consider differnce between 
# odd and even length
# Runtime: O(n^2)
# Spacetime: O(1)

class Solution:

    def longestPalindrome(self, s: str) -> str:

        res = ""
        res_len = 0

        for i in range(len(s)):
            l, r = i, i

            # Move pointer outwards (odd numbers)
            while(l >= 0 and r < len(s)):
                if(s[l] != s[r]):
                    break
                
                if(len(s[l:r+1]) > res_len):
                    res = s[l:r+1]
                    res_len = len(res)
                
                l -= 1
                r += 1
            
            # Now check for even palindroms
            l, r = i, i+1
            while(l >= 0 and r < len(s)):
                if(s[l] != s[r]):
                    break
                
                if(len(s[l:r+1]) > res_len):
                    res = s[l:r+1]
                    res_len = len(res)
                
                l -= 1
                r += 1

        return res

# Runtime: O(n^3) - we can have up to n^2 substrings, and palindrome check takes O(n)
# Space: O(n) - depth of recursion stack
# Problem: Our palindrome check gives us an extra O(n) runtime, so we end up with O(n^3)

from functools import cache

class Solution:

    """ Helper function to check wether given string is palindrome"""
    def palindrome(self, s: str) -> bool:
        return s == s[::-1]

    @cache
    def longestPalindrome(self, s: str) -> str:

        # Base case: String has length of 1
        if len(s) == 1:
            return s
        # Check if current string palindrome
        palindrome = self.palindrome(s)

        # Else check current length
        current = len(s) if palindrome else 0
        left_side = self.longestPalindrome(s[:len(s)-1])
        right_side = self.longestPalindrome(s[1:len(s)])
        
        result = ""

        if current == max(current, len(left_side), len(right_side)):
            result = s
        elif len(left_side) == max(current, len(left_side), len(right_side)):
            result = left_side
        else:
            result = right_side
        
        return result
