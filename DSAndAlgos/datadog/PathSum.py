# Runtime: O(n), n being the number of nodes in the the tree
# Space: O(k), k recursion stack depth 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        # Base case: Is val 0 and leaf?
        if not root.left and not root.right:
            print("Found correct leaf!")
            return targetSum - root.val == 0

        print(targetSum - root.val)
        # If not, reduce targetSum
        # pass down left side, and right side
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
