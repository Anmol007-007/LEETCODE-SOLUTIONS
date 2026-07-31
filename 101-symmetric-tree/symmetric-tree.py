# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que=deque([(root.left,root.right)])
        while que:
            node1,node2= que.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val!=node2.val:
                return False
            que.append((node1.left,node2.right))
            que.append((node1.right, node2.left))
        
        return True