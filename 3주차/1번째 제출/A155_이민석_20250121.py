#PPS "A155"
def max_lan_length(k, n, lengths):
    left, right = 1, max(lengths) 
    result = 0

    while left <= right:
        mid = (left + right) // 2  # 중간값
        count = sum(l // mid for l in lengths)
        
        if count >= n: 
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)] 

print(max_lan_length(k, n, lengths))
'''
이 문제는 이진탐색을 이용해 구현해봤다
랜선의 길이를 이진 탐색을 통해 좁혀가면서
가능한 최대 길이를 탐색하게 하였다
시간복잡도를 낮추기 위해서 이진탐색을 사용했다
자른 랜선의 개수가 n이상일 경우 현재값 즉 중간값이 가능한 최대 길이가 된다
이때 결과 값을 중간값으로 갱신하고 더 긴길이를 찾기 위해 왼쪽 값을 증가시킨다
'''