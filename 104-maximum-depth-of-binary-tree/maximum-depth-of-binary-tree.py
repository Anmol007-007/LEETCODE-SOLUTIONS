# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth=0
        qu=deque([root])
        
        while qu:
            depth+=1
            for i in range(len(qu)):
                node = qu.popleft()
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
        return depth