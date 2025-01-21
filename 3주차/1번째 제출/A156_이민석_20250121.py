#PPS "A156"
def find_max_height(trees, m):
    left, right = 0, max(trees)  # 절단기 높이의 범위
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total_wood = sum(tree - mid for tree in trees if tree > mid) 
        
        if total_wood >= m:  # 충분히 나무를 얻은 경우
            result = mid 
            left = mid + 1 
        else:  # 나무가 부족한 경우
            right = mid - 1 

    return result

n, m = map(int, input().split()) 
trees = list(map(int, input().split()))  

print(find_max_height(trees, m))
#이진 탐색

'''
이진탐색을 활용하여 풀었다
확실히 max min과 같은 문법이 있으니 문제를 접근하기 편한 것 같다
'''