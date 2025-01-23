#PPS "B021"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node):
            if node:
                inorder(node.left)  # 왼쪽 자식 방문
                result.append(node.val)  # 현재 노드 방문
                inorder(node.right)  # 오른쪽 자식 방문
        
        inorder(root)
        return result