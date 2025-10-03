# Naive approach: We iterate over every array field, slice it together with a 
# special sign and then go through the string and slice it up at the special sign
# Time complexity: O(m) + O(n) = O(m+n) (m length array, n length string)
# Space complexity: O(m) + O(n) = O(m+n)

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"
        return "###-###".join(strs)

    def decode(self, s: str) -> List[str]:
        # Special marker to represent an empty list
        if s == "#":  
            return []
        return s.split("###-###")
