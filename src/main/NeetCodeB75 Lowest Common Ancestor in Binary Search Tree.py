# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We are working on a binary search tree not a normal binary Tree, we can use its properties 
# to make our lifes easier 
# Runtime: O(h), height of the tree
# Spacetime O(h), height of the tree

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        if p.val < root.val and q.val > root.val:
            return root
        if p.val > root.val and q.val < root.val:
            return root

        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This solution works for general binary trees! However we are dealing with a binary search tree which we use to our advantage here.
# Runtime: O(h), h depth of the three
# Spacetime: O(h)

class Solution:

    def find_value(self, root: TreeNode, val: int) -> bool:
        if root is None: 
            return False
        if root.val == val:
            return True
        else:
            return self.find_value(root.left, val) or self.find_value(root.right, val)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        q_left_side = False
        q_right_side = False
        p_left_side = False
        p_right_side = False

        # If p or q is root we can not go any lower
        if p.val == root.val:
            return root
        if q.val == root.val:
            return root
        # Find out wether p and q are on the same or different side for this root
        q_left_side = self.find_value(root.left, q.val)
        q_right_side = self.find_value(root.right, q.val)
        p_left_side = self.find_value(root.left, p.val)
        p_right_side = self.find_value(root.right, p.val)
        # If p and q are on different sides, root must be LCA
        if (q_left_side and p_right_side) or (q_right_side and p_left_side):
            return root 
        else:
            if root.left and root.right:
                return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
            elif root.left:
                return self.lowestCommonAncestor(root.left, p, q)
            elif root.right:
                return self.lowestCommonAncestor(root.right, p, q)
