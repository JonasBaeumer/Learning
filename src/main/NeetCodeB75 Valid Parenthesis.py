# Optimized approach:
# If open bracket add to stack
# If closed bracket: Check if stack empty -> False, if at the end of string len(stack) > 0 -> False
# Runtime: O(n) one iterations through list
# Spacetime: O(n) worst case size of stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        open_brackets = ["[", "{", "("]
        valid_combinations = ["[]", "{}", "()"]

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if len(stack) > 0:
                    brackets = stack.pop() + char
                    if brackets not in valid_combinations:
                        return False
                else:
                    return False
        
        if len(stack) > 0:
            return False
        return True
