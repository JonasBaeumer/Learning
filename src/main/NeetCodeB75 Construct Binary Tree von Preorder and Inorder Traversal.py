# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # If there is only a leaf left, we have reached the end of this tree
        if len(preorder) == 1:
            return root
        root_inorder_index = 0
        # Find root element position in inorder list
        for i, value in enumerate(inorder):
            if value == preorder[0]:
                root_inorder_index = i

        # We know first element in preorder is root
        # Now find where left side in preorder ends
        left_subtree_size = root_inorder_index
                
        root.left = self.buildTree(preorder[1:1+left_subtree_size], inorder[0:root_inorder_index])
        root.right = self.buildTree(preorder[1 + left_subtree_size:], inorder[root_inorder_index+1:])

        return root 
