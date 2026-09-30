# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []

        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        arr.pop(len(arr) - n)

        if len(arr) == 0:
            return None
        
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]

        arr[-1].next = None 

        return arr[0]