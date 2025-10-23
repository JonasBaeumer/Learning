# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Get all values in this BST with BFS, then sort the list and return index k-1
# Runtime: O(n log n), extra log n for sorting
# Spacetime: O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        queue = deque()
        queue.append(root)
        value_list = []

        while queue:
            level_size = len(queue)
            operations_counter = 0
            while operations_counter < level_size:
                # Pop element
                node = queue.pop()
                # Add value to our list
                value_list.append(node.val)
                # Add left and right to queue
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                operations_counter += 1

        print(value_list)
        value_list = sorted(value_list)
        
        return value_list[k-1]
