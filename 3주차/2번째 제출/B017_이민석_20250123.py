#PPS "B017"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 기저 사례: root가 None이면 None을 반환
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        # 왼쪽과 오른쪽 자식에 대해서도 invertTree를 재귀적으로 호출
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
'''
이 재귀함수의 기저 상황은 ROOT가 NONE이면 NONE을 반환하는 것이다
왼쪽과 오른쪽 자식 노드에 대해서도 invertTree를 재귀적으로 호출해야한다
'''