# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        max_seen = root.val

        def dfs(root,max_seen):
            res = 0
            if not root:
                return 0

            if root.val >= max_seen:
                res +=1
                max_seen = max(max_seen,root.val)

            return res + dfs(root.right,max_seen) + dfs(root.left,max_seen)

        return dfs(root,max_seen)

        