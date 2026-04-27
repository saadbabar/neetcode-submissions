"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        my_dict = {}

        cur = head
        while cur:
            my_dict[cur] = Node(cur.val) # this map the old node to the new one
            cur = cur.next

        cur = head
        while cur:
            new_node = my_dict[cur]
            new_node.next = my_dict.get(cur.next) # get gets the value associate with key
            new_node.random = my_dict.get(cur.random)
            cur = cur.next
        return my_dict[head]