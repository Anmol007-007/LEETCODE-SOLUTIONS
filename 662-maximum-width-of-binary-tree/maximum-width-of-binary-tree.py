# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([(root,0)])
        maxwidth=0
        while que:
            first = que[0][1]
            last = que[-1][1]
            maxwidth = max(maxwidth,last-first+1)
            for i in range(len(que)):
                node,idx = que.popleft()
                curr_idx = idx-first
                if node.left:
                    que.append((node.left,2*curr_idx))
                if node.right:
                    que.append((node.right,2*curr_idx+1))
        return maxwidth