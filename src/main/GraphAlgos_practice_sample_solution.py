"""
==========================
 GRAPH PRACTICE SHEET
==========================
"""

from collections import deque

###############################################################
# 1. Build adjacency list (undirected)
###############################################################

def build_adj_undirected(n, edges):
    adj = {i: [] for i in range(n)}
    for left,right in edges:
        adj[left].append(right)
        adj[right].append(left)
    
    return adj

explain_undirected = """
In undirected graphs, we have to add both direction of the edge to our adj. list
While it might seem like adding one direction is enough, since we should
be able to traverse the graph coming from one direction only, we do not have
control over which edge we will insert, this could create situations where we
are adding the "wrong" direction only which will lead to the graph appearing 
disconnected during our traversal when it is in fact connected. 
"""

# === TESTS ===
print("TEST 1 UNDIRECTED:", build_adj_undirected(3, [[0,1],[1,2]]) == {
    0:[1], 1:[0,2], 2:[1]
})
print("TEST 2 UNDIRECTED:", build_adj_undirected(3, []) == {
    0:[],1:[],2:[]
})

###############################################################
# 2. Build adjacency list (directed)
###############################################################

def build_adj_directed(n, edges):
    adj = {i: [] for i in range(n)}
    for left, right in edges:
        adj[left].append(right)
    return adj

explain_directed = """
Here we only have a single direction that we can follow to explore the graph.
To ensure it is connected we might have to start from different starting points,
or a root node (if possible) which allows us to reach every place in the graph.
"""

# === TESTS ===
print("TEST 1 DIRECTED:", build_adj_directed(3, [[0,1],[1,2]]) == {
    0:[1], 1:[2], 2:[]
})
print("TEST 2 DIRECTED:", build_adj_directed(3, []) == {
    0:[],1:[],2:[]
})

###############################################################
# 3. DFS traversal template (Only about exploring, not cycles detection, validation, etc.)
# Traversal: works for directed *or* undirected graphs
###############################################################

# global structures for this exercise
adj = {0:[1],1:[2],2:[]}
visited = [False]*3

def dfs_template(node):
    if visited[node]:
        return
    
    visited[node] = True
    for node in adj[node]:
        dfs_template(node)
    
explain_dfs = """
Here we only want to explore/traverse the graph to reach all nodes, we dont care about 
detecting cycles, validating trees, etc.
"""

# === TESTS ===
visited = [False]*3
dfs_template(0)
print("TEST DFS:", visited == [True,True,True])

###############################################################
# 4. BFS traversal template
# Traversal: works for directed *or* undirected graphs
###############################################################

# global structures for this exercise
adj = {0:[1,2],1:[3],2:[],3:[]}

def bfs_template(start):
    queue = deque()
    queue.append(start)
    visited = set()
    # TODO: BFS using a queue
    while queue:
        node = queue.popleft() 
        # Why not queue.pop?
        # Because that would make it LIFO (last in first out), so this is just non recursive DFS
        # .popleft() gives us FIFO (first in first out) for BFS
        visited.add(node)
        
        for neighbor in adj[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                
    return list(visited)

explain_bfs = """
Instead of exploring on path on the tree until its end we explore our graph or tree
level by level, only after each level is finished will we continue further
"""

# === TESTS ===
res = bfs_template(0)
print("TEST BFS:", set(res) == {0,1,2,3})

###############################################################
# 5. Cycle detection (UNDIRECTED)
###############################################################

# global structures for this exercise
adj = {0:[1],1:[0,2],2:[1]}
visited = [False]*3

def has_cycle_undirected(node, parent):
    
    # Base case: We have visited this node before and its not direct parent
    # -> cycle
    if visited[node]:
        return True
    visited[node] = True
    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        else:
            if has_cycle_undirected(neighbor, node):
                return True
    
    return False

explain_cycle_undirected = """
TODO
"""

# === TESTS ===
visited=[False]*3
print("TEST UNDIRECTED NO CYCLE:", has_cycle_undirected(0,-1)==False)

adj = {0:[1],1:[0,2],2:[1,0]}
visited=[False]*3
print("TEST UNDIRECTED CYCLE:", has_cycle_undirected(0,-1)==True)

###############################################################
# 6. Cycle detection (DIRECTED)
###############################################################

# global structures for this exercise
adj = {0:[1],1:[2],2:[]}
state = [0]*3   # 0=unvisited,1=visiting,2=done

def has_cycle_directed(node):
    # Base case 1: Its on our path that we are exploring -> cycle
    if state[node] == 1:
        return True
    # Base case, we have already explored this path
    if state[node] == 2:
        return False
    
    state[node] = 1
    for neighbor in adj[node]:
        if has_cycle_directed(neighbor):
            return True
    state[node] = 2
    return False

explain_cycle_directed = """
TODO
"""

# === TESTS ===
state = [0]*3
print("TEST DIRECTED NO CYCLE:", has_cycle_directed(0)==False)

adj = {0:[1],1:[2],2:[1]}
state = [0]*3
print("TEST DIRECTED CYCLE:", has_cycle_directed(0)==True)

###############################################################
# 7. Topological Sort
###############################################################

# global structures for this exercise
adj = {0:[1],1:[2],2:[]}
n = 3
visited = [False]*n
order = []

def topo_sort():
    # TODO
    pass

explain_toposort = """
TODO
"""

# === TESTS ===
visited=[False]*3; order=[]
topo_sort()
print("TEST TOPO SIMPLE:", order in ([0,1,2],[0,2,1]))

###############################################################
# 8. Connected Components
###############################################################

# global structures for this exercise
adj = {0:[1],1:[0],2:[],3:[4],4:[3]}
visited = [False]*5

def connected_components():
    # TODO
    pass

explain_components = """
TODO
"""

# === TESTS ===
visited = [False]*5
print("TEST COMPONENTS:", connected_components()==3)

###############################################################
# 9. Bipartite Check
###############################################################

# global structures:
adj = {0:[1],1:[0,2],2:[1]}
color = [-1]*3

def is_bipartite():
    # TODO
    pass

# === TESTS ===
color = [-1]*3
adj = {0:[1],1:[0,2],2:[1]}
print("TEST BIPARTITE TRUE:", is_bipartite()==True)

color = [-1]*3
adj = {0:[1],1:[0,2],2:[1,0]}
print("TEST BIPARTITE FALSE:", is_bipartite()==False)

###############################################################
# 10. Grid DFS
###############################################################

DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
visited = set()

def dfs_grid(r,c,grid):
    # TODO
    pass

# === TESTS ===
grid = [
 [1,1],
 [0,1]
]
visited=set()
dfs_grid(0,0,grid)
print("TEST GRID:", visited == {(0,0),(0,1),(1,1)})

###############################################################
# 11. Valid Tree
###############################################################

def is_tree(n, edges):
    # TODO
    pass

explain_tree = """
TODO
"""

# === TESTS ===
print("TEST TREE TRUE:", is_tree(5,[[0,1],[0,2],[0,3],[1,4]])==True)
print("TEST TREE FALSE:", is_tree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]])==False)

###############################################################
# 12. Pitfalls
###############################################################

common_pitfalls = """
TODO: write 5
"""
