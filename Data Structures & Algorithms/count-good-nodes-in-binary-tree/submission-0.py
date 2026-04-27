# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, root.val)])
        count = 1
        while queue:
            node, value = queue.popleft()

            if node.left:
                if node.left.val >= value:
                    count += 1
                    queue.append((node.left, node.left.val))
                else:
                    queue.append((node.left, value))

            if node.right:
                if node.right.val >= value:
                    count += 1
                    queue.append((node.right, node.right.val))
                else:
                    queue.append((node.right, value))
            
        return count

            