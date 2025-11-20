# Optimized approach: we encode the length of each string as a delimitter, 
# When decoding this way we know how many positions in the string we can skip.
# Even if the actual string also contains delimitters and numbers this will not cause 
# a problem because the first part of the string will be our true length + delimitter
# this way, we will directly jump to the next numbers, so fake delimitters will never actually
# be read. The # must follow after the length encoding so that we can read multi digit numbers
# and still know when to stop

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Iterate through array and before string encode length
        if not strs:
            return "#"
        s = ""
        for entry in strs:
            s += (str(len(entry))+"#"+entry)
        return s


    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        res, i, n = [], 0, len(s)
        while i < n:
            # read length up to '#'
            j = i
            while j < n and s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res

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
