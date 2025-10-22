# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Idea: Use BFS to check for each root weather all nodes below it on the left side are smaller
# and all nodes on the right are bigger
# If valid subtree move down to the next level and check for the root nodes there
# Runtime: O(n * n), worst case
# Spacetime: O(n)

class Solution:

    def left_side_smaller(self, root: Optional[TreeNode], val: int) -> bool:
        if root is None:
            return True
        if root.val >= val:
            return False
        
        return self.left_side_smaller(root.left, val) and self.left_side_smaller(root.right, val)
    
    def right_side_bigger(self, root: Optional[TreeNode], val: int) -> bool:
        if root is None:
            return True
        if root.val <= val:
            return False
        
        return self.right_side_bigger(root.right, val) and self.right_side_bigger(root.left, val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_side = self.left_side_smaller(root.left, root.val)
        right_side = self.right_side_bigger(root.right, root.val)

        if left_side and right_side:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
