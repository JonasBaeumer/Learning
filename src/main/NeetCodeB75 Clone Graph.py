"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# For BFS the trick is different, here we have to make sure by the time we see the node in the original
# graph our copies of the node are already created. 
# That means we have to create our original copies in the hashtable the first time we encounter them
# and that is when we look at the neighborhood of its adjacent nodes.
# Make sure that you also check that for the very first node! Or otherwise the first node will only
# be connected one directional so the first node doesnt know the rest of the graph exists 
# Runtime: O(V+E), we have to iterate over all nodes, and visit all its neighbors (edges)
# Spacecomplexity: O(V) for the hashmap that stores references to the copies 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
         # Do it with DFS

         # Traverse the graph with dfs for each point add a new node to our graph 
         # Also here remember which nodes we have already visited so that we dont repeat ourselves
        if node is None:
            return node

        hashmap_old_new = {}
        queue = deque()
        queue.append(node)

        while queue:
            current_node = queue.pop()
            if current_node not in hashmap_old_new:
                hashmap_old_new[current_node] = Node(current_node.val)
            for neighbor in current_node.neighbors:
                # If we see a neighbor for the first time, create node and add it to queue and hm
                if neighbor not in hashmap_old_new.keys():
                    hashmap_old_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Regardless, connect the current clone to the neighbor’s clone
                hashmap_old_new[current_node].neighbors.append(hashmap_old_new[neighbor])

        return hashmap_old_new[node]  

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Traverse the graph with DFS (dont need to do level by level however here)
# Make sure to check wether node has already been visited to avoid loops
# Current problem: How do I deal with the issue of making actual copies or neighbors, 
# then moving towards the neighbor objects but then reference back to the original copy instead
# of the old one to make sure they point at the right references.
# Trick: We actually need to have hashmap that will track wether we have already created a copy for 
# the respective original node. On the very first object creation, we actually dont create any neighborhood
# we only start creating the neighborhood after our discovery is finished and we have created the copies
# Runtime: O(V+E), we have to iterate over all nodes, and visit all its neighbors (edges)
# Spacecomplexity: O(V) for the hashmap that stores references to the copies 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
         # Do it with DFS

         # Traverse the graph with dfs for each point add a new node to our graph 
         # Also here remember which nodes we have already visited so that we dont repeat ourselves
        if node is None:
            return node

        hashmap_old_new = {}

        def dfs(node):
            # Base case: We already have the copy present to we can directly store it
            if node in hashmap_old_new:
                return hashmap_old_new[node]
            
            # If it is not present we need to create a new node and store it
            node_copy = Node()
            node_copy.val = node.val
            hashmap_old_new[node] = node_copy
            
            # now we need to run the traversal again to fill up the nighbors once they are ready
            for neighbor in node.neighbors:
                hashmap_old_new[node].neighbors.append(dfs(neighbor))

            # Now return the node we have created
            return node_copy

        return dfs(node)    
