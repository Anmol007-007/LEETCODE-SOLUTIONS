# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans=[]
        que=deque([root])
        parent={}
        while que:
            for i in range(len(que)):
                node=que.popleft()
                if node.left:
                    parent[node.left.val]=node
                    que.append(node.left)
                if node.right:
                    parent[node.right.val]=node
                    que.append(node.right)
        visited={}
        que.append(target)
        while k>0 and que:
            for i in range(len(que)):
                node=que.popleft()
                visited[node.val]=1
                if node.left and node.left.val not in visited:
                    que.append(node.left)
                if node.right and node.right.val not in visited:
                    que.append(node.right)
                if node.val in parent and parent[node.val].val not in visited:
                    que.append(parent[node.val])
            k-=1
        while que:
            ans.append(que.popleft().val)
        return ans