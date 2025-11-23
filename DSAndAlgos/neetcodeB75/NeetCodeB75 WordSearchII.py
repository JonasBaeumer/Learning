"""
First thoughts:
One idea would be to build up the priefix tree once with the grid.
Then for each word we could just check wether it can be constructed or not.
Problem: We have duplicates and dictionaries must have unique keys.

Naive approach:
For each of the words, id go through the whole 2d array and then start
the search at all possible starting points and explore the array from there
Problem: Very inefficient, O(n*m) for finding all starting points, O(k^4) since we
can move in four different directions (or 3/2 on the outer layer).
Problem: When exploring the path for a word we can not reuse or revisit the 
same cell twice. 

Can I somehow build a datastructure from this 2D grid that allows me to 
navigate all possible word combinations in constant or linear time?
Building up the datastructure once would take O(n*m) but thats ok as long
as that is a one time effort. 
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Recursive function that we use to explore the graph
        def dfs(i, j, word, visited_cells) -> bool:
            # Base case: we have an empty word (e.g. we found the right one)
            if not word:
                return True
            # We have to make sure that we are not revisiting a cell that we have seen before
            if (i, j) in visited_cells:
                return False
            # We could step out of bounds / explore a direction that is beyond the grid
            # which is not allowed
            if i < 0 or j < 0 or i >= len(board) or j >= len(board):
                return False
            # If the current position does not match the first character of the word 
            # we are exploring a wrong path
            if board[i][j] != word[0]:
                return False
            # Now we have to explore all four directions
            results = []
            visited_cells.append((i, j))
            results.append(dfs(i - 1, j, word[1:], visited_cells))
            results.append(dfs(i + 1, j, word[1:], visited_cells))
            results.append(dfs(i, j - 1, word[1:], visited_cells))
            results.append(dfs(i, j + 1, word[1:], visited_cells))

            return any(results)

        # Go through each of the starting points in our 2D grid and if the 
        # character matches, initialize search from this point
        found_words = []
        for word in words:  
            for i in range(len(words)):
                for j in range(len(words)):
                    if dfs(i, j, word, []):
                        found_words.append(word)
        
        return found_words
