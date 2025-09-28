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
