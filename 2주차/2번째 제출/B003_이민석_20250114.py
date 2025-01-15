#PPS "B003"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
         # 예외 처리: 빈 트리일 경우
        if not root:
            return 0

        # 왼쪽 리프 노드인지 판별하는 함수
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        total_sum = 0

        if root.left:
            if is_leaf(root.left):  
                total_sum += root.left.val 
            else:
                total_sum += self.sumOfLeftLeaves(root.left)

        if root.right:
            total_sum += self.sumOfLeftLeaves(root.right)

        return total_sum
        
        """
            
        """