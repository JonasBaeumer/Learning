# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: O(n), number of nodes in the tree because we need to visit each node once
# Space: O(k), k recursion stack depth / depth of tree 

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        running_sum = 0

        def dfs(node):
            nonlocal running_sum
            # Base case: Essentially we go beyond the tree so nothing to return 
            if not node:
                return
            
            # Explore right side
            dfs(node.right)
            # Add running sum to val
            running_sum += node.val
            node.val = running_sum
            # Explore left side
            dfs(node.left)
        
        dfs(root)
        return root
