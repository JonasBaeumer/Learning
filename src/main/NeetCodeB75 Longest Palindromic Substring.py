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
