# Optimized approach: We go through the list, and remember the last node for each node change 
# the next pointer to the last node and move to the next 
# Runtime O(n)
# Spacetime O(1) or O(n) if you consider out linkedlist

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        current_node = head

        while(current_node is not None):
            temp = current_node.next
            current_node.next = last_node
            last_node = current_node
            current_node = temp
        
        return last_node
