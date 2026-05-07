# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        
        temp = []
        while queue:
            level = len(queue)   
            while len(temp) < level:
                first = queue.popleft()
                temp.append(first.val)
                if first.left:
                    queue.append(first.left)
                  
                if first.right:
                    queue.append(first.right)
            
            res.append(temp)
            temp = []
            


        return res
        