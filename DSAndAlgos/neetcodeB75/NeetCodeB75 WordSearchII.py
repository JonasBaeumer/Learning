from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False      # Marks that a dictionary word ends here
        self.has_word = False    # Marks that this word was actually found on the board

    def add(self, word: str) -> None:
        if not word:
            self.is_end = True
            return
        ch = word[0]
        if ch not in self.children:
            self.children[ch] = TrieNode()
        self.children[ch].add(word[1:])

    def find(self, word: str) -> bool:
        if not word and self.is_end:
            return True
        elif not word or word[0] not in self.children:
            return False
        return self.children[word[0]].find(word[1:])
    
    def find_all_words(self, prefix: str = "") -> List[str]:
        """
        Return all words in this trie for which `has_word` is True.
        """
        result: List[str] = []

        def dfs(node: "TrieNode", path_chars: List[str]) -> None:
            # Only record words that were actually found on the board
            if node.has_word:
                result.append("".join(path_chars))

            for ch, child in node.children.items():
                path_chars.append(ch)
                dfs(child, path_chars)
                path_chars.pop()

        dfs(self, list(prefix))
        return result
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the trie from the word list
        trie = TrieNode()
        for word in words:
            trie.add(word)

        rows, cols = len(board), len(board[0])

        def dfs(i: int, j: int, node: TrieNode) -> None:
            # Out of bounds
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return

            ch = board[i][j]

            # Already visited cell
            if ch == "#":
                return

            # This path doesn't exist in the trie
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # If this node completes a dictionary word, mark it as found
            if next_node.is_end:
                next_node.has_word = True

            # Mark current cell as visited
            board[i][j] = "#"

            # Explore neighbors
            dfs(i - 1, j, next_node)
            dfs(i + 1, j, next_node)
            dfs(i, j - 1, next_node)
            dfs(i, j + 1, next_node)

            # Restore the cell (backtrack)
            board[i][j] = ch

        # Start DFS from every cell on the board
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)

        # Collect all words that were found (has_word == True)
        return trie.find_all_words()

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

# Runtime: O(l) * O(n*m) * O(3^k) = O(l * n * m * 3^k)
# l number of words, n*m dimensions of grid, k length of individual word
# Space: O(k), k is the recursion stack depth / length of the word
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
            # Important: We need to backtrack our cell here to ensure that we 
            # allow other parts of the exploration to visit it we only wanted to mark 
            # it for the current path of our exploration
            visited_cells.pop()

            return any(results)

        # Go through each of the starting points in our 2D grid and if the 
        # character matches, initialize search from this point
        found_words = set()
        for word in words:  
            for i in range(len(words)):
                for j in range(len(words)):
                    if dfs(i, j, word, []):
                        found_words.add(word)
        
        return list(found_words)
