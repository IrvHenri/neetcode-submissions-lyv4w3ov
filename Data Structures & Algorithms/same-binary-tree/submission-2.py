# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        

        queue =  deque([p,q])
        

        while queue:
            
            node_p = queue.popleft()
            node_q = queue.popleft()

            if node_p and node_q:
                
                if node_p.val != node_q.val:
                    return False
                else:
                    queue.append(node_p.left)
                    queue.append(node_q.left)
                    queue.append(node_p.right) 
                    queue.append(node_q.right)
            elif node_p == node_q:
                continue
            else:
                return False

        return True