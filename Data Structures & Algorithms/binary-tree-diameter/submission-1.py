# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dfs(root):
            nonlocal res

            if not root:  # empty node has height 0 (no edges)
                return 0

            # Get the maximum depths of left and right subtrees
            left = dfs(root.left)  # height of left subtree
            right = dfs(root.right)  # height of right subtree

            # The longest path through current node = left + right edges
            # Update global maximum if this path is longer
            res = max(res, left + right)

            # Return height of current node: 1 (edge to parent) + max child height
            return 1 + max(left, right)

        dfs(root)
        return res

