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
    # TODO: fill in
    return adj

explain_undirected = """
TODO
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
    # TODO: fill in
    return adj

explain_directed = """
TODO
"""

# === TESTS ===
print("TEST 1 DIRECTED:", build_adj_directed(3, [[0,1],[1,2]]) == {
    0:[1], 1:[2], 2:[]
})
print("TEST 2 DIRECTED:", build_adj_directed(3, []) == {
    0:[],1:[],2:[]
})

###############################################################
# 3. DFS traversal template
###############################################################

def dfs_template(node, adj, visited):
    # TODO
    pass

explain_dfs = """
TODO
"""

# === TESTS ===
adj = {0:[1],1:[2],2:[]}
visited = [False]*3
dfs_template(0, adj, visited)
print("TEST DFS:", visited == [True,True,True])

###############################################################
# 4. BFS traversal template
###############################################################

def bfs_template(start, adj):
    # TODO
    pass

explain_bfs = """
TODO
"""

# === TESTS ===
adj = {0:[1,2],1:[3],2:[],3:[]}
print("TEST BFS:", bfs_template(0, adj) in ([0,1,2,3],[0,2,1,3]))

###############################################################
# 5. Cycle detection (UNDIRECTED)
###############################################################

def has_cycle_undirected(node, parent, adj, visited):
    # TODO
    pass

explain_cycle_undirected = """
TODO
"""

# === TESTS ===
adj = {0:[1],1:[0,2],2:[1]}
visited=[False]*3
print("TEST UNDIRECTED NO CYCLE:", has_cycle_undirected(0,-1,adj,visited)==False)

adj = {0:[1],1:[0,2],2:[1,0]}
visited=[False]*3
print("TEST UNDIRECTED CYCLE:", has_cycle_undirected(0,-1,adj,visited)==True)

###############################################################
# 6. Cycle detection (DIRECTED)
###############################################################

def has_cycle_directed(node, adj, state):
    # TODO
    pass

explain_cycle_directed = """
TODO
"""

# === TESTS ===
adj = {0:[1],1:[2],2:[]}
print("TEST DIRECTED NO CYCLE:",
      has_cycle_directed(0,adj,[0]*3)==False)

adj = {0:[1],1:[2],2:[1]}
print("TEST DIRECTED CYCLE:",
      has_cycle_directed(0,adj,[0]*3)==True)

###############################################################
# 7. Topological Sort
###############################################################

def topo_sort(n, adj):
    # TODO
    pass

explain_toposort = """
TODO
"""

# === TESTS ===
adj = {0:[1],1:[2],2:[]}
print("TEST TOPO SIMPLE:",
      topo_sort(3, adj) in ([0,1,2],[0,2,1]))

###############################################################
# 8. Connected Components
###############################################################

def connected_components(n, adj):
    # TODO
    pass

explain_components = """
TODO
"""

# === TESTS ===
adj = {0:[1],1:[0],2:[],3:[4],4:[3]}
print("TEST COMPONENTS:", connected_components(5, adj)==3)

###############################################################
# 9. Bipartite Check
###############################################################

def is_bipartite(n, adj):
    # TODO
    pass

# === TESTS ===
adj = {0:[1],1:[0,2],2:[1]}
print("TEST BIPARTITE TRUE:", is_bipartite(3,adj)==True)

adj = {0:[1],1:[0,2],2:[1,0]}
print("TEST BIPARTITE FALSE:", is_bipartite(3,adj)==False)

###############################################################
# 10. Grid DFS
###############################################################

DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs_grid(r,c,grid,visited):
    # TODO
    pass

# === TESTS ===
grid = [
 [1,1],
 [0,1]
]
visited=set()
dfs_grid(0,0,grid,visited)
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
