# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, l1

        while cur:
            nxt_node = cur.next
            cur.next = prev
            prev = cur
            cur = nxt_node
        l1 = prev
        
        prev2, cur = None, l2

        while cur:
            nxt_node = cur.next
            cur.next = prev2
            prev2 = cur
            cur = nxt_node
        l2 = prev2

        string1 = ""
        string2 = ""

        while l1:
            string1 += str(l1.val)
            l1 = l1.next
        while l2:
            string2 += str(l2.val)
            l2 = l2.next

        num = int(string1) + int(string2)
        num = str(num)
        save_node = None
        head = None
        for i in range(len(num) - 1, -1, -1):
            new_node = ListNode(int(num[i]))
            if save_node:
                save_node.next = new_node
                save_node = new_node
            else:
                save_node = new_node
                head = save_node
        return head
