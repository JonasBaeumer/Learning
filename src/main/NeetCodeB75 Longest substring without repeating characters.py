 # Optimized approach: Use dictionary to keep track in indices of all seen letters
# Once duplicate is realized measure distance (right-left) and move left pointer
# to duplicate position + 1
# Runtime: O(n)
# Spacetime: O(m) -> Length of longest substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_seen = {}
        longest_sequence = 0
        left = 0

        for right in range(len(s)):
            if s[right] in character_seen and character_seen[s[right]] >= left:
                distance = right - left
                left = character_seen[s[right]]+1
                character_seen[s[right]] = right
                if distance > longest_sequence:
                    longest_sequence = distance
            else:
                character_seen[s[right]] = right
                distance = right - left + 1
                if distance > longest_sequence:
                    longest_sequence = distance
        
        return longest_sequence

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
