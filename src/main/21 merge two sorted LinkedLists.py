# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case if one or both lists are empty
        result = None

        if (not list1 and not list2):
            return None
        elif (not list1):
            return list2
        elif (not list2):
            return list1

        tail = None

        pointer1 = list1
        pointer2 = list2

        first_element = True
        
        while (pointer1 and pointer2):
            if pointer1.val <= pointer2.val:
                if (first_element):
                    first_element = False
                    result = pointer1
                    tail = result
                    pointer1 = pointer1.next
                else:
                    tail.next = pointer1
                    pointer1 = pointer1.next
                    tail = tail.next
            else:
                if (first_element):
                    first_element = False
                    result = pointer2
                    tail = result
                    pointer2 = pointer2.next
                else:
                    tail.next = pointer2
                    pointer2 = pointer2.next
                    tail = tail.next

        if (pointer1):
            tail.next = pointer1
        else: 
            tail.next = pointer2

        return result
