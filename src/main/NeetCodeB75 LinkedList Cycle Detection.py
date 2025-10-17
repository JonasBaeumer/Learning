# Optimized approach: Use two pointers who run at different speeds to track wether
# there is a cycle or not, if there is they will overlap at some point
# Runtime: O(n)
# Spacetime: O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head

        while pointer1 and pointer1.next:
            pointer1 = pointer1.next.next
            pointer2 = pointer2.next
            if pointer1 == pointer2:
                return True

        return False

# Optimized approach: Use two pointers who run at different speeds to track wether
# there is a cycle or not, if there is they will overlap at some point
# Same code just a bit rewritten
# Runtime: O(n)
# Spacetime: O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head

        while(pointer1):
            pointer1 = pointer1.next.next if pointer1.next is not None else pointer1.next
            pointer2 = pointer2.next
            if not pointer1:
                return False
            if (pointer1 == pointer2):
                return True

        return False

# Optimized approach: Use two pointers who run at different speeds to track wether
# there is a cycle or not, if there is they will overlap at some point
# Runtime: O(n)
# Spacetime: O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head

        while(pointer1):
            pointer1 = pointer1.next
            if pointer1:
                pointer1 = pointer1.next
            pointer2 = pointer2.next
            if (pointer1 is None):
                return False
            if (pointer1 == pointer2):
                return True

        return False

# Initial approach: Store elements in memory to remember what we have already seen
# Runtime: O(n)
# Spacetime: O(n) -> need to store every seen node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_notes = set()

        while(head):
            if (head in seen_notes):
                return True
            else:
                seen_notes.add(head)
                head = head.next

        return False
