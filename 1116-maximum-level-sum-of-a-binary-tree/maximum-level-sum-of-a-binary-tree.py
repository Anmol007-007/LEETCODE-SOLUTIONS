# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        que=deque([root])
        maxi,max_lvl=float("-inf"),0
        curr_lvl=0
        while que:
            lvl=len(que)
            s=0
            for i in range(lvl):
                node=que.popleft()
                s+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            curr_lvl+=1
            if s>maxi:
                maxi=s
                max_lvl=curr_lvl
        return max_lvl