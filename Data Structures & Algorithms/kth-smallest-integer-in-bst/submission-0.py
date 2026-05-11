# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # preorder traversal root, left then right. store in arr. access kth element - 1.
        stack = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
            
        dfs(root)
        print(stack)
        return stack[k-1]
            

        