from collections import Counter
import re

# Runtime: O(n), scan whole string and replace characters
# Spacetime: O(u), for the hashmap u number of individual words

class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # First edit the string to remove all unecessary signs and we can replace them with ' '
        
        words_lowercase = re.sub(r'[^a-zA-Z ]', ' ', paragraph).lower()

        words = words_lowercase.split(" ")

        words_hm = Counter(words)

        # Get word that appears most and check that it does not appear in banned

        for word in banned:
            if word in words_hm:
                words_hm[word] = 0

        words_hm[''] = 0

        print(words_hm.items())
        max_pair = ("", 0)
        for key,value in words_hm.items():
            if value > max_pair[1]:
                max_pair = (key, value)
            

        return max_pair[0]
