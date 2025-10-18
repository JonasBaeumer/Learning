# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(n) * O(k) = k length of the lists
# Spacetime: O(1) just pointers

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        merged_list = ListNode()
        tail = merged_list
        index = -1
        current_node = None
        # We will move our pointers along the actual given list in place (no extra datastructure needed)

        # Outer loop that runs while all first pointer are not None:
        while any(node is not None for node in lists):
            
            current_node = None
            index = -1
            # Loop over all the lists and check if all the pointer are non None
            # Find the lowest value to append
            for i in range(len(lists)):
                if lists[i] is not None:
                    if current_node is None or lists[i].val <= current_node.val:
                        current_node = lists[i]
                        index = i
                        
            # Add the element to our tail and cut the chain to the next element (=None) and
            # Move the pointer in that list to the next element
            tail.next = current_node
            tail = tail.next
            lists[index] = lists[index].next

        return merged_list.next
