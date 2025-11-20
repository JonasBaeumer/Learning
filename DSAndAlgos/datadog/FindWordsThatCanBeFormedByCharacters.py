
from collections import Counter

class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:

        length = 0
        # Build our frequency dict
        chars_count = Counter(chars)

        # For each word in words:
        for word in words:
            
            is_true = True
            # Build our own frequency List
            word_count = Counter(word)

            # Check each letter in the word
            for key, value in word_count.values():
                if value > chars_count[key]:
                    is_true = False
                    break
            
            if is_true:
                length += len(word)

            # If frequency word > letter: -> We are missing a character can tbe added
        
        return length

  # Runtime: O(k) -> Length of all words combined in the list
# Spacetime: O(1/26) -> Hashmap has to store all characters in the worst case

class Solution:

    def buildHashMap(self, s):
        chars_count = {}
        for char in s:
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1 
        return chars_count

    def countCharacters(self, words: List[str], chars: str) -> int:
        # Build up the hashmap with character frequencies from chars:
        chars_count = self.buildHashMap(chars)
        print(chars_count)

        length = 0

        # Go over all the words in words:
        for word in words:
            
            is_good = True
            # For each word, build frequency hashmap
            word_count = self.buildHashMap(word)
            # Go over each key in frequency hashmap and check if 
            for key, value in word_count.items():
                if chars_count.get(key, 0) >= value:
                    continue
                else:
                    is_good = False
                    break
            
            if is_good:
                length += len(word)
                
        return length
