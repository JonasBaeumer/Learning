# Idea we can just treat the edges as one directional we can run dfs through the graph 
# Idea: Model graph as adjacency list and run DFS to explore for cycles
# While running DFS, keep track of all the nodes you have seen 
# If seen_nodes < n (graph disconnected)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen_nodes = [False] * n
        adj_list = {i: [] for i in range(n)}

        # Build adjacency list for modeling undirected graph
        for left, right in edges:
            adj_list[left].append(right)
            adj_list[right].append(left)

        # Return True if we have a cycle
        def dfs(node, parent):
            # Base case 1: We have a cycle
            if seen_nodes[node]:
                return True
        
            seen_nodes[node] = True
            # Set node status to 1 (on current path)
            for edge in adj_list[node]:
                if parent == edge:
                    continue
                if dfs(edge, node):
                    return True
            
            return False

        if dfs(0, -1) or not all(seen_nodes):
            return False 
        return True
