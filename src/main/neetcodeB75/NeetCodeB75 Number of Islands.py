# Runtime: O(n*m), because we visit each field exactly once
# Spacetime: O(n*m), because we stored each visited field
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        COLS, ROWS = len(grid), len(grid[0])
        if not grid:
            return 0
        
        visited_coordinates = set()
        number_of_islands = 0

        for i in range(COLS):
            for j in range(ROWS):
                if (i,j) not in visited_coordinates and grid[i][j] == "1":
                    # BFS
                    queue = deque()
                    queue.append((i,j))
                    # If all position in the queue are empty, we have explored the island
                    while queue:
                        current_level = len(queue)
                        operations_counter = 0
                        while operations_counter < current_level:
                            # Retrieve element
                            col_row = queue.pop()
                            col, row = col_row[0], col_row[1]
                            visited_coordinates.add((col, row))
                            # Find its adjacent elements
                            directions = [(1,0), (-1,0), (0,1), (0,-1)]
                            for dcol, drow in directions:
                                new_col, new_row = col + dcol, row + drow
                                if 0 <= new_col < COLS and 0 <= new_row < ROWS:
                                    if (new_col, new_row) not in visited_coordinates \
                                       and (new_col, new_row) not in queue \
                                       and grid[new_col][new_row] == "1":
                                        queue.append((new_col, new_row))
                            operations_counter += 1
                    number_of_islands += 1

        return number_of_islands 
