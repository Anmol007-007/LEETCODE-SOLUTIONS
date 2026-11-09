# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        self.maxi=0
        def dfs(node,is_left,l):
            if not node:
                return 
            self.maxi=max(self.maxi,l)
            if is_left:
                dfs(node.right,False,l+1)
                dfs(node.left,True,1)
            else:
                dfs(node.right,False,1)
                dfs(node.left,True,l+1)
        dfs(root.left,True,1) if root.left else None
        dfs(root.right,False,1) if root.right else None
        return self.maxi