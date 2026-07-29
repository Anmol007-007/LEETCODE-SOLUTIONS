from collections import defaultdict,deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack=[]
        que=deque([(root,0,0)])
        while que:
            node,row,col = que.popleft()
            stack.append((col,row,node.val))
            if node.left:
                que.append((node.left,row+1,col-1))
            if node.right:
                que.append((node.right,row+1,col+1))
        stack.sort()
        ans=defaultdict(list)
        for col,row,node in stack:
            ans[col].append(node)
        return list(ans.values())