#PPS "B009"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0
            
            leftHeight = checkHeight(node.left)
            rightHeight = checkHeight(node.right)
            
            if leftHeight == -1 or rightHeight == -1:
                return -1
            
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            return max(leftHeight, rightHeight) + 1
        
        return checkHeight(root) != -1
'''
재귀함수를 통해서 높이를 계산했다 서브트리가 불균형이면 -1을 반환하였다
굳이 함수를 작성할 필요가 없을 수 있지만 전체 코드를 작성하는것이 아니라 하나의 클래스 안에서 함수를 작성해야하다보니
이런식으로 재귀함수를 사용한 것 같다
왼쪽 오른쪽 높이를 게속 체크하면서 답을 구하였다.
'''