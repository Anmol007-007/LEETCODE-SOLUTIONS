class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        stack = []
        node = root
        last_visited = None
        heights = {None: 0} 
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    node = peek_node.right
                else:
                    left_h = heights[peek_node.left]
                    right_h = heights[peek_node.right]

                    if abs(left_h - right_h) > 1:
                        return False
                        
                    heights[peek_node] = 1 + max(left_h, right_h)
                    
                    last_visited = stack.pop()
                    
        return True