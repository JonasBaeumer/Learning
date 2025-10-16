# Optimized solution: Go through both lists simultaneously and check wether 
# which value is bigger (as long as one list non empty)
# Runtime O(n+m)
# Spacetime O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = ListNode()
        merged_list_node = merged_list
        list1_node = list1
        list2_node = list2

        while(list1_node is not None or list2_node is not None):
            
            if list1_node is not None and list2_node is not None:
                if (list1_node.val <= list2_node.val):
                    merged_list_node.next = list1_node
                    list1_node = list1_node.next
                else:
                    merged_list_node.next = list2_node
                    list2_node = list2_node.next
            elif list1_node is None:
                merged_list_node.next = list2_node
                list2_node = list2_node.next
            else:
                merged_list_node.next = list1_node
                list1_node = list1_node.next

            merged_list_node = merged_list_node.next

        return merged_list.next
