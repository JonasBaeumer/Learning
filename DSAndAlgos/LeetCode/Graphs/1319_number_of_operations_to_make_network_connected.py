"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible return -1.
"""

"""
Goal: Find out if i can move redundant edges in a network to other place such that we connect the whole graph

Idea: Do union find, to build up the network. If I see that a node already has the same parent, then I know the edge is unnecessary and I can 
increase the counter. After I have build up the whole network, I can check how many connected components there are and I need (n-1) edges to connect
them together
"""
test_input_n = 4
test_connections = [[0,1],[0,2],[1,2]]
test_input_n_two = 6
test_connections_two = [[0,1],[0,2],[0,3],[1,2],[1,3]]

# Run: find, worstcase O(V) 2, meanin 2V, Union-loop: O(E) -> O(E*2V) = O(E*V)
# Space: O(V) for parents, rest variables O(1) -> O(V)

def makeConnected(n: int, connections: list[list[int]]) -> int:
	connected_components = n
	parents = list(range(n)) # 0 ... n-1	

	def find(x):
		if parents[x] == x:
			return x
		return find(parents[x])
	
	# Do union find to build graph but remember to count how many edges were "unecessary"
	redundant_edges = 0
	for a,b in connections:
		a_parent = find(a)
		b_parent = find(b)
		if a_parent != b_parent: # Edge is needed for connecting the network, we are merging two connected components
			connected_components -= 1
			parents[b_parent] = a_parent
		else: # Edge is redundant, must count!
			redundant_edges += 1

	# Count connected components
	# If we have n connected components and n-1 unnecessary edges -> Good
	if connected_components - 1 <= redundant_edges:
		return connected_components - 1
	else:
		return -1
print(makeConnected(test_input_n, test_connections))
print(makeConnected(test_input_n_two, test_connections_two))
print(makeConnected(test_input_n_two, [[0,1],[0,2],[0,3],[1,2]]))
			
		
