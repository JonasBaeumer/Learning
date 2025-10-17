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
