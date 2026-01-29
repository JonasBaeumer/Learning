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
"""

test_list = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

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
	return
	
	# Do DFS traversal (add each node to visited while doing that)
	
print(removeStones(test_list))
	
