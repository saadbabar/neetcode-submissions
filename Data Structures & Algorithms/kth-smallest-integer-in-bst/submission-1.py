# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        my_list = [] 

        def dfs(root):
            nonlocal my_list
            if not root:
                return

            dfs(root.left)
            my_list.append(root.val)
            dfs(root.right)

        dfs(root)
        return my_list[k - 1]
