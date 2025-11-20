# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use BFS algorithm to explore the tree 
# Base case: We have reached a node that is empty
# Runtime: O(n), nodes in the tree
# Space complexity: O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + right if left < right else 1 + left
