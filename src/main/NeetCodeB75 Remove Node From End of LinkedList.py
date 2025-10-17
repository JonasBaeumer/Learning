# Approach: We first have to determine the length of our list again before we know at which position we can remove the element
# (relative to the start). Since for normal removal we need to know the prev, current and next element we first need to cover 
# a bunch of edge cases to avoid Null pointer errors (e.g. first element, list size 1, last element)
# Then we can remove the element and return our start pointer
# Runtime: O(n) + O(n) = O(2n) -> O(n)
# Spacetime: O(1) just need to keep track of the respective pointers
# Same approach just cleaned up the end since next is not needed at the end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        end = head

        while end.next:
            length += 1
            end = end.next

        # Calculate the relative position from the start that we should remove
        remove_index = length - n

        if remove_index == 0 and length == 1:
            return None
        elif remove_index == 0:
            return head.next

        prev = None
        current = head
        # Navigate to node that should be removed
        for _ in range(remove_index):
            prev = current
            current = current.next

        # Remove element
        prev.next = current.next

        return head

# Approach: We first have to determine the length of our list again before we know at which position we can remove the element
# (relative to the start). Since for normal removal we need to know the prev, current and next element we first need to cover 
# a bunch of edge cases to avoid Null pointer errors (e.g. first element, list size 1, last element)
# Then we can remove the element and return our start pointer
# Runtime: O(n) + O(n) = O(2n) -> O(n)
# Spacetime: O(1) just need to keep track of the respective pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        end = head

        while end.next:
            length += 1
            end = end.next

        # Calculate the relative position from the start that we should remove
        remove_index = length - n

        if remove_index == 0 and length == 1:
            return None
        elif remove_index == 0:
            return head.next

        prev = None
        current = head
        # Navigate to node that should be removed
        for _ in range(remove_index):
            prev = current
            current = current.next
        
        if not current.next:
            next = None
        else:
            next = current.next
        
        # Remove element
        prev.next = next

        return head
