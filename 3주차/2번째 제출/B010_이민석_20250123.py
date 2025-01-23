#PPS "B010"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # 트리의 최대 지름

        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter

'''
트리의 최대 지름을 구하는 것인데, 트리의 지름은 트리에서 가장 긴 경로의 길이를 의미한다
또한 두개의 리프 노드를 포함해야한다
각 노드를 기준으로 왼쪽 깊이, 오른쪽 깊이를 구한 후 두 깊이를 더하면 그 노를 포함하는 트리의 최대 지름을 알 수 있다
처음에 이 부분을 떠오르기 너무 오래걸려서 문제를 풀기 힘들었다.
'''