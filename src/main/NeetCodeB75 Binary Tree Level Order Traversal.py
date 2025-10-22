# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Go through the tree level by level with BFS, use lenght per level to know how many node should 
# be gone through from the queue
# Spacetime: O(n), n nodes in the list
# Space complexity: O(n), n nodes in the list

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        traversal=[]

        while(len(queue) != 0):
            # Take length of current queue so we know when to stop and nodes are from next level
            number_of_elements_for_level = len(queue)
            operations_counter = 0
            sublist = []
            if not root:
                return []

            while(operations_counter < number_of_elements_for_level):
                # Pop element
                node = queue.popleft()
                # Add left and right to queue
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                # Add val of element to our list
                sublist.append(node.val)
                operations_counter += 1

            # When length reached
            traversal.append(sublist)

        return traversal
