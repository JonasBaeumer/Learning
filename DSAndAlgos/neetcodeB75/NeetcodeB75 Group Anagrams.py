# Use the ord function which gives the unicode function to normalize it to create a positional array to allow counting how many times each character occurs
# Runtime: O(n) + O(m) = O (n + m)
# Spacetime: O(m)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Keep a hashmap of store of sorted anagrams
        memory = {}

        # Loop over strs and sort each string on appearance
        for string in strs:

            count = [0] * 26
            for i in range(len(string)):
                index = ord(string[i]) - ord('a')
                count[index] += 1

            if "".join(str(count)) in memory:
                memory["".join(str(count))].append(string)
            else:
                memory["".join(str(count))] = [string]
        
        return list(memory.values())

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
