# Approach: DFS to explore once we found a possible start point, remember indexes we have visited and 
# remove them on the way back to free them up again for the next search
# Runtime:
# -> MxN cells on the board 
# -> Max number of recursive calls we can make is l, length of the word
# -> We can branch into three new direction, 3
# -> O(mn3^l)
# Spacetime: O(l), length of the word
# Idea for improvement?
# -> Can we somehow eliminate all fields that are not part of the actual string so we dont need to branch them?

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited_positions = set()
        
        def dfs(board, current_string, word, i, j):
            # base case:
            # 1. We found the word
            if current_string == word:
                return True
            # 2. We overshot and our word is now too long
            if len(current_string) > len(word):
                return False
            # 3. If we would step outside our board:
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return False
            # 4. If we are revisiting a position that we have been to before
            if (i,j) in visited_positions:
                return False
            
            new_string = current_string + board[i][j]
            visited_positions.add((i,j))
            # Explore all three directions
            search_left = dfs(board, new_string, word, i, j+1)
            search_right = dfs(board, new_string, word, i, j-1)
            search_up = dfs(board, new_string, word, i-1, j)
            search_down = dfs(board, new_string, word, i+1, j)
            # If we are backtracking dont forget to remove the position again
            visited_positions.remove((i,j))

            return search_left or search_right or search_up or search_down

            
            
        # Loop over the array to ensure we explore with DFS from only viable starting points
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, "", word, i, j):
                        return True
        return False
