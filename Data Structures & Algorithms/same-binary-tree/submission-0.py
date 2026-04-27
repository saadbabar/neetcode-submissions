# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # pre-order traversal and check if they are the same
        def pre_order(root, nums):

            if root is None:
                nums.append(-1)
                return
            nums.append(root.val)
            pre_order(root.left, nums)
            pre_order(root.right, nums)

            return nums
        
        nums1 = []
        nums2 = []
        pre_order(p, nums1)
        pre_order(q, nums2)

        return nums1 == nums2
