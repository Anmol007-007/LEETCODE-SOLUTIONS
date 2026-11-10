# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if not root:
            return 0
        self.ans=0
        def dfs(node,curr):
            if not node:
                return 
            curr+=node.val
            if curr==targetSum:
                self.ans+=1
            dfs(node.left,curr)
            dfs(node.right,curr)
        que=deque([root])
        while que:
            node=que.popleft()
            dfs(node,0)   
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return self.ans