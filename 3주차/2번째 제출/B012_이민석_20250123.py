#PPS "B012"
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node is None:
        return []
    result = postorder_traversal(node.left)
    result += postorder_traversal(node.right)
    result.append(node.val)
    return result

def build_tree(preorder, start, end):
    if start > end:
        return None
    
    root = TreeNode(preorder[start])
    split_index = start + 1
    while split_index <= end and preorder[split_index] < root.val:
        split_index += 1

    root.left = build_tree(preorder, start + 1, split_index - 1)
    root.right = build_tree(preorder, split_index, end)
    
    return root

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

root = build_tree(arr, 0, len(arr) - 1)
postorder_result = postorder_traversal(root)
print(" ".join(map(str, postorder_result)))

'''
트리 노드를 가지는 클래스를 따로 정의하였다
같이 코드를 리뷰하는 친구의 코드에서 영감을 받았다
다른 문제였지만 클래스를 정의하여 문제를 해결하니 코드의 재활용성이 좋아진 느낌이 들었다
왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 만들며 트리를 구성하는 방식으로 구현하였다.
'''