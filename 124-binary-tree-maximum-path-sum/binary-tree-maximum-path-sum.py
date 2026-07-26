# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=-float("inf")
        def path(node):
            if not node:
                return 0
            left_p=max(0,path(node.left))
            right_p=max(0,path(node.right))

            summ=node.val+left_p+right_p
            self.maxsum=max(self.maxsum,summ)
            return max(left_p,right_p)+node.val
        path(root)
        return self.maxsum