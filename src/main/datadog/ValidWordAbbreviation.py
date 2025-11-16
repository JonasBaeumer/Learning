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
