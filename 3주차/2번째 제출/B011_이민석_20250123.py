#PPS "B011"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        merged = TreeNode(root1.val + root2.val)
        
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged

'''
두개의 트리를 병합해야한다 나느 그래서 재귀적으로 트리의 각 노드를 합쳐나갔다
첫번째 트리가 비어있으면 두번째 트리를 그대로 반환하고 반대의 경우는 반대로 해줘야하는 부분을
구현하지 않아 꽤 오래 걸렸다.
'''