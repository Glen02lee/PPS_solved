#PPS "B018"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:=
        if not root:
            return False
        
        # 리프 노드에 도달한 경우, 현재 값이 targetSum과 일치하는지 확인
        if not root.left and not root.right:
            return root.val == targetSum
        
        # 왼쪽과 오른쪽 자식으로 각각 탐색
        targetSum -= root.val  # 현재 노드 값을 빼주고
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))

'''
현재 노드가 none이면 경로가 존재하지 않다는 것이 기저상황이다
리프 노드에 도달한 경우 현재 값이 targetSum과 일치하는지 확인하며
왼쪽, 오른쪽 자식으로 탐새하며 리턴값을 정해준다.
'''