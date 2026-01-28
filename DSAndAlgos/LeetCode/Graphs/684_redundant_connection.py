"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
"""

"""
Approach: We do Union-Find to build up the graph. If the graph is a tree each node can only be connected to the graph by one node. If we 
ever want to add an edge and the node is already connected to the graph, then we have a redundant node
"""

# Runtime: O(V + E)
# Space: O(V)

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
	n = len(edges)
	parents = list(i in range(n) + 1)

	def find(x: int) -> int:
		if parents[x] == x:
			return x
		return find(parents[x])
	
	edge = [-1, -1]
	for a, b in edges:
		a_root = find(a)
		b_root = find(b)
		if a_root != b_root:
			parent[b_root] = a_root
		else: # This node is already connected must be the additional edge
			edge = [a, b]
	return edge
			

