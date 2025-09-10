# Naive approach
# Runtime: O(n) x O(1) x O(k log k) sorting -> O(n k log(k))
# Spacetime: O(n * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Keep a hashmap of store of sorted anagrams
        memory = {}

        # Loop over strs and sort each string on appearance
        for string in strs:

            # If sorted string in hashmap, add original string to it as value
            if "".join(sorted(string)) in memory:
                memory["".join(sorted(string))].append(string)

            else: # Else make new entry with sorted key and add value
                memory["".join(sorted(string))] = [string]
        
        return list(memory.values())
