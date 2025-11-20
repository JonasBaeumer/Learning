class Solution:

# Have two pointers

# Have a char hash table where we check for each letter in the string if it is contained already in the hashtable

    # If not contained add it to the hastable and move second pointer forward

    # If contained: Move first pointer forward by one and calculate difference between both pointers

    def lengthOfLongestSubstring(self, s: str) -> int:

        first_pointer = 0
        second_pointer = 0

        longest_substring = 0;

        char_hash_map = {}

        while(second_pointer < len(s)):

            if s[second_pointer] in char_hash_map:
                if (longest_substring < second_pointer - first_pointer):
                    longest_substring = second_pointer - first_pointer
                first_pointer+=1
                second_pointer = first_pointer
                char_hash_map = {}
            else:
                char_hash_map[s[second_pointer]] = 1
                second_pointer+=1
                if (longest_substring < second_pointer - first_pointer):
                    longest_substring = second_pointer - first_pointer
        
        return longest_substring
