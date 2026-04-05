from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(node):
            nonlocal res
            if not node or res:
                return
            
            if node.val == subRoot.val:
                if self.bfs(node, subRoot):
                    res = True
                    return
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res

    def bfs(self, root, subRoot):
        queue = deque([(root, subRoot)])

        while queue:
            node_root, node_subRoot = queue.popleft()
            
            if not node_root and not node_subRoot:
                continue
            if not node_root or not node_subRoot or node_root.val != node_subRoot.val:
                return False
            
            queue.append((node_root.left, node_subRoot.left))
            queue.append((node_root.right, node_subRoot.right))
        return True
        # 