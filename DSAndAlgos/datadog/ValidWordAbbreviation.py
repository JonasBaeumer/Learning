# Runtime O(n)
# Space: O(1), only two numbers and temp numbers

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0

        while i < len(abbr):

            # Is the current char a digit?
            if abbr[i].isdigit():
                # Check if leading 0 -> Yes, return False
                if abbr[i] == "0":
                    return False

                # Build the full number
                number = 0
                while i < len(abbr) and abbr[i].isdigit():
                    number = number * 10 + int(abbr[i])
                    i += 1

                # Move j pointer up by number
                j += number

                # Check if j > len(word) -> Yes, return False 
                if j > len(word):
                    return False

            # If not check if they are equal and move both pointers
            else:

                if j >= len(word) or abbr[i] != word[j]:
                    return False

                i += 1
                j += 1
        
        return j == len(word)

# THIS SOLUTION DOESNT WORK

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        steps_abbreviated = 0
        total_chars = 0
         
        # loop through the abbreviation:
        for i in range(len(abbr)):
            print(i)
            char = abbr[i]
            if str.isdigit(char):
                if char == 0:
                    return False
                # Track the length of the number we are looking at 
                j = i
                while str.isdigit(abbr[j]):
                    total_chars += 1
                    j+=1
                print(abbr[i:j])
                number = int(abbr[i:j])
                # Now we can check is the number valid? 
                if number > 20:
                    return False
                # If number valid, check if we are jumping out of bounds
                if i + steps_abbreviated >= len(word):
                    return False
                steps_abbreviated += number
                i = j
        #BUG Loop will overwrite whatever value reset we have in the inner function!

        print(steps_abbreviated + total_chars)
        if steps_abbreviated + total_chars != len(word):
            return False
        return True
