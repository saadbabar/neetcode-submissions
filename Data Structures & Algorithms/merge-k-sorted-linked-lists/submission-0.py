# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]

        
        while len(lists) > 1:
            dummyNode = ListNode()
            cur = dummyNode
            list1, list2 = lists[0], lists[1]
            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
                    
            while list1:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            while list2:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

            lists.pop(0)
            lists.pop(0)
            lists.append(dummyNode.next)

        return lists[0]
                