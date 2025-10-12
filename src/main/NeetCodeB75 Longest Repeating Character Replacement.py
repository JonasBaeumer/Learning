

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
