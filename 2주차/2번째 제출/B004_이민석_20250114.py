#PPS "B004"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 트리가 비어있다면 대칭임
        if not root:
            return True

        # 두 개의 서브트리를 비교하는 함수 DFS로 구현하였음
        def is_mirror(t1, t2):
            # 둘 다 None이면 대칭
            if not t1 and not t2:
                return True
            # 하나만 None이면 대칭 아님
            if not t1 or not t2:
                return False
            # 현재 노드 값이 같고, 서브트리들이 거울 대칭인지만 확인하면 됨.
            return (t1.val == t2.val) and \
                   is_mirror(t1.left, t2.right) and \
                   is_mirror(t1.right, t2.left)

        return is_mirror(root.left, root.right)