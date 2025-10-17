# Naive approach: We loop through the list so we now the midpoint and end and then 
# use two pointers to "reweb" the list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        end = head
        length = 1
        start = head

        while end.next:
            end = end.next
            length += 1

        middle = length // 2
        current_node = head
        middle_element = start

        for i in range(middle):
            middle_element = middle_element.next

        # Break the Link
        tmp = middle_element.next
        middle_element.next = None
        middle_element = tmp

        second_half = None
        # Reverse second half
        while(middle_element is not None):
            temp = middle_element.next
            middle_element.next = second_half
            second_half = middle_element
            middle_element = temp

        while second_half is not None:
            tmp = current_node.next
            current_node.next = second_half
            current_node = tmp

            tmp = second_half.next
            second_half.next = current_node
            second_half = tmp
