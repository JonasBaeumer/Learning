class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        array = list(s)
        last_space = 0
        current_space = 0
        last_was_space = True
        length = 0

        for index, char in enumerate(array):

            if not last_was_space:
                if char == ' ':
                    length = index - current_space
                    last_was_space = True
            else:
                if char != ' ':
                    current_space = index
                    last_was_space = False
        
        if not last_was_space:
            length = len(array) - current_space
        
        return length
