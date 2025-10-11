# Naive approach: Nested loop for each letter forward to find longest sequence
# Runtime: O(n^2 worst case)
# Timecomplexity: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_seen = set()
        longest_sequence = 0

        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            character_seen = set()
            for j in range (i, len(s), 1):
                if s[j] in character_seen:
                    distance = j-i
                    if distance > longest_sequence:
                        longest_sequence = distance
                    break
                else:
                    distance = j-i+1
                    if distance > longest_sequence:
                        longest_sequence = distance
                    character_seen.add(s[j])
        
        return longest_sequence
