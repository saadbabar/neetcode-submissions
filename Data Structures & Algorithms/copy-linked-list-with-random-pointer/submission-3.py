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
        # make a deep copy
        if not head: return
        cur = head
        my_map = {}
        while cur:
            new_node = Node(cur.val)
            my_map[cur] = new_node
            cur = cur.next
        cur = head

        while cur:
            new_node = my_map[cur]
            new_node.next = my_map.get(cur.next)
            new_node.random = my_map.get(cur.random)
            cur = cur.next
        return my_map[head]
            
        