# Other approach: Merge two Linked Lists repeatedly

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Optimized approach: Our outer loop can not be improved since we need to make sure that we have
# looked at each element in lists at least once since it needs to be appended
# Inner loop however is inefficient, we are doing a lot of duplicate work since we are only changing
# a single pointer each iteration while the rest stays the same
# Optimize this with a min heap/priority queue -> O log k
# Runtime: O(n) * O(log kk) = k number of lists in lists, n number of nodes that I am appending in total
# Spacetime: O(k) for heap

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # Merge the two lists together
        while(len(lists)) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeLists(list1, list2))
            lists = merged_lists
        
        return lists[0]

    
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy 
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(n) * O(k) = k number of lists in lists, n number of nodes that I am appending in total
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
