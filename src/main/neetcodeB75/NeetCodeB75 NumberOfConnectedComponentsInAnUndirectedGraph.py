# Simple DFS with tracking of connected components
# Runtime: O(V+E)
# Spacetime: O(V+E)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for left, right in edges:
            adj[left].append(right)
            adj[right].append(left)

        visited = [False] * n

        def dfs(node):
            # Base case, we have reached a node that we have seen before
            if visited[node]:
                return 
            
            visited[node] = True
            for neighbor in adj[node]:
                dfs(neighbor)
        
        connected_components = 0
        for node in adj.keys():
            if not visited[node]:
                connected_components += 1
                dfs(node)

        return connected_components
