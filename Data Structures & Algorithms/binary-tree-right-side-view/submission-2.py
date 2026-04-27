# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        queue = collections.deque([root])

        while queue:
            q_len = len(queue)
            right_node = None
            for i in range(q_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    right_node = node.left
                if node.right:
                    queue.append(node.right)
                    right_node = node.right
            if right_node:
                res.append(right_node.val)
        return res
