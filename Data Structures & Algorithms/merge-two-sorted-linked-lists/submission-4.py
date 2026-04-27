# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        cur = dummyNode

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        # while list1:
        #     cur.next = list1
        #     # dont need to iterate the rest of the nodes, just connect cur.next to the remaining
        # while list2:
        #     cur.next = list2

        cur.next = list1 if list1 else list2


        return dummyNode.next
