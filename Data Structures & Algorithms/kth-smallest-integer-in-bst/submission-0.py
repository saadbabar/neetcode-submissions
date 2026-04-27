# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque([root])
        pq = []

        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    heapq.heappush(pq, -node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        while len(pq) > k:
            heapq.heappop(pq)
        
        return abs(pq[0])
            

            