# Now here we are trying to check for each string if the current word is present or not

from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(index):
            
            # Base case1: we have reached the end of the string we are done
            if index >= len(s):
                return True

            # For each word in wordDict -> explore next option and move index
        
            for word in wordDict:
                if s[index:index+len(word)] != word:
                    continue
                if dfs(index + len(word)):
                    return True
            
            return False
        
        return True if dfs(0) else False


# What is the issue on this solution: When we have long overlapping string until we get to a solution
# we generate long overlapping pairs of strings that we dont need and that kill our solution / memory.
# Essentially we are asking ourselves the wrong questions here: We are asking: "Which words can I build with
# this dict?", but we should ask: "Given the current position I am at is there a word in the dict that 
# matches it"
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(generated_str):
            
            # Base case1: String matches perfectly, found valid solution
            if generated_str == s:
                return 1

            # Base case2: We have overshot string length, so done exploring
            if len(generated_str) >= len(s):
                return 0

            # For each word in wordDict -> add word to dict and explore subproblem
            result = 0
            for word in wordDict:
                result = max(result, dfs(generated_str + word))
            
            return result
        
        return True if dfs("") else False
"""
This solution fails because it breaks for long complex problems

run.sh: line -11:    13 Killed                  python3 script.py

Input:

s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict=["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
Expected output:

false
"""
