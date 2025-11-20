# Optimized solution: Do check for valid character at runtime to reduce required space to O(1)
# Spacecomplexity: O(1)
# Runtime: O(n)
class Solution:
    is_alnum = re.compile(r'[A-Za-z0-9]').match          

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.is_alnum(s[i]):
                i += 1
            while i < j and not self.is_alnum(s[j]):
                j -= 1
            if i < j and s[i].casefold() != s[j].casefold():
                return False
            i += 1
            j -= 1
        return True

# Spacecomplexity: n (new version of the string) + 2 (for each pointer) = n
# Runtime:  n/2 + n/2 + n (dont now how long sub and lower methods needs (probably need to iterate over whole string) = n

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_string = re.sub(r'[^A-Za-z0-9]', '', s.lower().replace(" ",""))
        print(lowercase_string)
        pointer_one = 0
        pointer_two = len(lowercase_string) - 1
        is_palindrome = True

        while(True):
            if (pointer_one > pointer_two):
                return True
            
            if (lowercase_string[pointer_one] != lowercase_string[pointer_two]):
                return False
            
            pointer_one += 1
            pointer_two -= 1
