# Explore graph with DFS
# Different cases:
# We have cells that are connected to pacific ocean (n=0, m=0-end)
# We have cells that are connected to atlantic ocean (n=0-end, m=0)
# What we are going to do is instead of running down from each of the cells to the ocean we are going to run up 
# from all cells that are directly adjacent to the ocean. So our DFS is going up not down
# We can use one DFS function and run it from two different starting sides (Atlantic, Pacific)
# Then we keep a list of all nodes that we reached while going up during both traversals
# Ultimately we return the nodes that are in both lists
# Runtime: O(m*n)
# Spacetime: O(m*n)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_nodes = set()
        pacific_nodes = set()
        result = []

        last_val = -1

        def dfs(i, j, ocean, last_val):
            # Base case: We reached water 
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]):
                return
            # Base case: Node is already in atlantic_nodes or pacific nodes
            if ((i,j) in atlantic_nodes and ocean == "atlantic") or ((i,j) in pacific_nodes and ocean == "pacific") :
                return
            # Base case: the value is smaller than the last seen node
            if heights[i][j] < last_val:
                return
            
            if ocean == "atlantic":
                atlantic_nodes.add((i, j))
            else:
                pacific_nodes.add((i, j))
            
            # Move left
            dfs(i, j-1, ocean, heights[i][j])
            # Move right
            dfs(i, j+1, ocean, heights[i][j])
            # Move up
            dfs(i-1, j, ocean, heights[i][j])
            # Move down 
            dfs(i+1, j, ocean, heights[i][j])

        # Start at all pacific adjacent nodes)
        for j in range(len(heights[0])):
            dfs(0, j, "pacific", last_val)
        # Go down left sides (pacific):
        for i in range(len(heights)):
            dfs(i, 0, "pacific", last_val)
            dfs(i, len(heights[0]) - 1, "atlantic", last_val)
        # Go right side bottom (atlantic)
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, "atlantic", last_val)
            
        for cell in atlantic_nodes:
            if cell in pacific_nodes:
                result.append([cell[0], cell[1]])

        return result
