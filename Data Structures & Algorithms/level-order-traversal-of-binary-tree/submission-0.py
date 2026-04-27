# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []

        while queue:
            list_output = []
            len_q = len(queue)

            for i in range(len_q):
                node = queue.popleft()
                if node:
                    list_output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if list_output:
                res.append(list_output)

        return res