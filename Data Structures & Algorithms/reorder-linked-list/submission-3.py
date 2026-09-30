# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Use slow fast pointers
        # 2. reverese list
        # 3. combine list

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of list from the end

        cur, prev = slow.next, None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        slow.next = None
        # head of first list, and head of second list
        list1, list2 = head, prev

        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next
            list1.next = list2
            list2.next = nxt1

            list1 = nxt1
            list2 = nxt2

        return