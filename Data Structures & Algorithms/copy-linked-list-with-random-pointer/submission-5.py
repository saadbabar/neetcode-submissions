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
        my_map = {}
        cur = head
        while cur:
            my_map[cur] = Node(x = cur.val)
            cur = cur.next

        # old node -> new node mapping

        cur = head
        while cur:
            my_map[cur].next = my_map.get(cur.next, None) # my_map[cur.next]
            my_map[cur].random = my_map.get(cur.random, None)
            cur = cur.next

        cur = head

        return my_map.get(cur, None)
