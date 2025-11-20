# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: O(n)
# Spacecomplexity: O(n)
# Approach: We first swap the two current children and then we go down in a DFS approach
# to swap the children of the children, etc.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # swap left and right
        if root is None:
            return None
        
        # recursively call invertTree for left and right
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
