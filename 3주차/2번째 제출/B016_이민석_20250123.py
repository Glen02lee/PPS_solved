#PPS "B016"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.new_root = None
        self.current = None
        
        def inorder(node):
            if node:
                inorder(node.left)
                if self.new_root is None:
                    self.new_root = TreeNode(node.val)
                    self.current = self.new_root
                else:
                    self.current.right = TreeNode(node.val)
                    self.current = self.current.right
                inorder(node.right)
        
        inorder(root)
        return self.new_root
