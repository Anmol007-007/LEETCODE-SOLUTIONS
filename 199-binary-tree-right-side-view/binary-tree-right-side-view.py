
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        que = deque([root])
        
        while que:
            lvl = len(que)
            
            for i in range(lvl):
                node = que.popleft()
                if i == lvl- 1:
                    res.append(node.val)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
        return res