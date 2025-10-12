# New approach: use a dict to determine for the current window size which character is most
# frequent to allow us to max out the window size 
# Runtime: O(n^2)
# Spacetime: O(1) since dict can have at max 26 values for the alphabet

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def sort_dict(d: dict) -> list:
            # Sort by frequency descending
            return sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))

        max_distance = 0

        for left in range(len(s)):
            frequency_dict = {}
            for right in range(left, len(s)):
                current_char = s[right]
                if current_char not in frequency_dict:
                    frequency_dict[current_char] = 1
                else:
                    frequency_dict[current_char] += 1

                sorted_dict = sort_dict(frequency_dict)
                max_freq = sorted_dict[0][1]
                window_size = right - left + 1

                if window_size - max_freq > k:
                    break

                max_distance = max(max_distance, window_size)

        return max_distance

# --------- DIDNT WORK!

# Naive approach: Double for loop, for each char move forward and see how many characters
# are different than our current one, once that number is bigger than k + 1 we must stop 
# and have the max length
# Issue: We are only taking forward moves into account, chars that we have already passed play
# no role anymore, s="ABBB", k=2, ex: Your Output: 3 Expected output: 4
# Idea: If reaching end of right while we dont have enough of chars, expand left? (kinda hacky
# dont like it)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        for i in range(len(s)):
            different_chars_counter = 0
            for right in range(i, len(s), 1):
                if (s[right] != s[i]):
                    different_chars_counter+=1
                if (different_chars_counter > k):
                    break
                distance = right-i+1
                if distance > max_length:
                    max_length=distance

        return max_length
