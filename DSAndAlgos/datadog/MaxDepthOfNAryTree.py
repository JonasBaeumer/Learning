"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(node):
            # Base case: We have reached the end of the tree
            if node is None:
                return 0
            total = 1
            for child in node.children:
                total = max(total, 1+dfs(child)) 
            return total

        return dfs(root)
