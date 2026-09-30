# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            length = length + 1
            cur = cur.next

        # case 1:
        if n == length:
            return head.next
        
        # case 2:
        if length == 1 and n == 1:
            return None
        
        # case 3:
        count = length - n
        cur = head
        for i in range(1, count):
            cur = cur.next
        cur.next = cur.next.next

        return head
