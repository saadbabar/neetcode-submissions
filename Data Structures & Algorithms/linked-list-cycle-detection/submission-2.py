# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        while head:
            if head not in my_set:
                my_set.add(head)
            else:
                return True
            head = head.next
        return False
