"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
"""

"""
Open questions:
	- I dont quite understand how to model the binary connection in the list datastructure
	
Approach:
	- First approach, we can use an adjacency list to traverse the graph and figure out the number of connected components
	- The number of elements we can remove is the the total number of stones - number of connected components

Bugs in first approach:
	- I think the adjacency list does not properly build a graph, it also build it if the stones are not set on the same column / row
	(example: (0,1), (1,0) neither of them can be removed but we would still draw an edge between them in the adj_list
		When do I consider an edge to have same col-row?
		How do I build my datastructure in a way that tells which jumps I can take and which I cant?
"""
from collections import defaultdict, deque

def removeStones(stones: list[list[int]]) -> int:
	n = len(stones)
	
	rows = defaultdict(list)
	cols = defaultdict(list)
	
	for idx, (x,y) in enumerate(stones):
		rows[x].append(idx)
		cols[y].append(idx)
	
	print(rows)
	print(cols)
	
	visited = set()
	components = 0
	
	for start in range(n):
		if start in visited:
			continue
		# DFS
		q = deque([start])
		visited.add(start)
		components += 1
	
		while q:
			i = q.popleft()
			x, y = stones[i]

			# visit all stones in the same row
			for nei in rows[x]:
				if nei not in visited:
					visited.add(nei)
					q.append(nei)
		
			# visit all stones in the same col
			for nei in cols[x]:
				if nei not in visited:
					visited.add(nei)
					q.append(nei)

			# Need to clear so we dont rescan this row/col over and over
			rows[x].clear()
			cols[y].clear()
	
	return n-components

test_list = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
removeStones(test_list)

def removeStones(stones: list[list[int]]) -> int:
	# First we have to build up our adjacency list
	# We also need to check which nodes we have already visited to not reexplore a already searched connected component
	
	# Build adjacency list
	adj_list = {}
	for a, b in stones:
		# if list is empty, create it
		if a not in adj_list:
			adj_list[a] = [b]
		if b not in adj_list:
			adj_list[b] = [a]
		# else add to existing
		else:
			if a not in adj_list[b]:
				adj_list[b].append(a)
			if b not in adj_list[a]:
				adj_list[a].append(b)
	
	print(adj_list)

	visited = set()
	from collections import deque
	def dfs(x: int):
		q = deque([x])
		while q:
			cur_element = q.popleft() # BFS
			visited.add(cur_element)
			for neighbor in adj_list.get(cur_element, []):
				if neighbor not in visited:
					q.append(neighbor) 
		return
	
	connected_components = 0
	for a,b in stones:
		if a not in visited:
			connected_components += 1
			dfs(a)
		if b not in visited:
			connected_components += 1
			dfs(b)
	print(connected_components)
	print(visited)
	return len(stones) - connected_components
	
	# Do DFS traversal (add each node to visited while doing that)
	
print(removeStones(test_list))
	
