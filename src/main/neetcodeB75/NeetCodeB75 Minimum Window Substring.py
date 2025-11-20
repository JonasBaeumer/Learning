# Already optimized with sliding window
# Runtime: O(n) + O(2m)
# Spacetime: O(2m) = O(m)

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def window_contains(s_count, t_count):
            for char in t_count:
                if s_count.get(char, 0) < t_count[char]:
                    return False
            return True

        t_chars_dict = {}
        # Initialize char array with all chars we need to check for
        for char in t:
            t_chars_dict[char] = t_chars_dict.get(char, 0) + 1

        s_chars_dict = {}

        left = 0
        right = 0
        min_len = float("inf")
        res = ""

        # 1. Grow the window until all of t chars appear at least once
        # 2. Shrink the window until at least one of the chars in t does not appear at all

        for right in range(len(s)):
            if s[right] in t_chars_dict:
                s_chars_dict[s[right]] = s_chars_dict.get(s[right], 0) + 1

            # shrink while window is valid
            while window_contains(s_chars_dict, t_chars_dict):
                # Update result
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]

                # Shrink
                if s[left] in t_chars_dict:
                    s_chars_dict[s[left]] -= 1
                left += 1

        return res
