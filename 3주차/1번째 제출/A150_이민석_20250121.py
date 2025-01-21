#PPS "A150"
def max_sum(n, arr):
    current_max = arr[0]
    global_max = arr[0]

    for i in range(1, n):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(global_max, current_max)

    return global_max

n = int(input())
arr = list(map(int, input().split()))

print(max_sum(n, arr))
'''
초기화를 한 후 배열을 순회하면서 최대 부분합을 갱신해야한다
현재 원소를 포함한 최대합 계산과 전체 최대합을 갱신하게 반복문을 작성하였다

'''