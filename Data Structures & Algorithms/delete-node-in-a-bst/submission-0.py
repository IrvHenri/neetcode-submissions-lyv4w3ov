# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val :
            root.left = self.deleteNode(root.left,key)
        else:
            
                copy_root = root
                right_child = copy_root.right
                left_child = copy_root.left

                if right_child and left_child:
                    curr = right_child
                    while curr.left:
                        curr = curr.left
                    curr.left = left_child
                    root = right_child
                elif right_child and not left_child:
                    root = right_child
                else:
                    root = left_child

        return root