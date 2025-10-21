# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Base case: We reached the end of the current subtree node
# If subrott.node is None -> return True
# For normal tree exploration: If we reach subroot -> return False
# What cases can we have. Current nodes match we go further down, they missmatch we continue with root
# Runtime: O(n) nodes of the tree * O(m) nodes in the subtree -> O(m * n)
# Spacetime: O(n + m )

class Solution:  

    def check_equal(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return self.check_equal(root.left, subRoot.left) and self.check_equal(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is not None:
            return False
        if root is None and subRoot is None:
            return True
        if root is not None and subRoot is None:
            return False
        
        # Nodes match -> Explore subtree phase
        if root.val == subRoot.val:
            left = self.check_equal(root.left, subRoot.left)
            right = self.check_equal(root.right, subRoot.right)
            if left and right:
                return True
        
        # Explore normal tree without subtree 
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
