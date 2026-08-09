class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_left_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        def get_right_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth
        
        left_d = get_left_depth(root)
        right_d = get_right_depth(root)
        
        if left_d == right_d:
            return (1 << left_d) - 1  
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)