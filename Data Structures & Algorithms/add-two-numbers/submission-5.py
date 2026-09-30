# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, 0)
        cur = dummyNode
        
        # l1 = [1, 7]
        # l2 = [4, 5, 6]
        carry = 0
        while (l1 and l2):
            summation = l1.val + l2.val + carry
            digit = summation % 10 
            cur.next = ListNode(val = digit)
            carry = 1 if (summation // 10 == 1) else 0
        
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            summation = l1.val + carry
            digit = summation % 10
            cur.next = ListNode(val = digit)
            carry = 1 if (summation // 10 == 1) else 0

            cur = cur.next
            l1 = l1.next

        while l2:
            summation = l2.val + carry
            digit = summation % 10
            cur.next = ListNode(val = digit)
            carry = 1 if (summation // 10 == 1) else 0

            cur = cur.next
            l2 = l2.next

        if (carry == 1):
            cur.next = ListNode(1)
            cur = cur.next

        return dummyNode.next

