#PPS "A153"
def min_waiting_time(n, times):
    times.sort() #정렬을 하여 계산하기
    
    total_time = 0
    accumulated_time = 0

    for time in times:
        accumulated_time += time
        total_time += accumulated_time

    return total_time

n = int(input())
times = list(map(int, input().split()))

print(min_waiting_time(n, times))

'''
누적합을 이용하면 된다고 생각했다
오름차순 정렬을 한 이후에 반복문을 통해 누적합을 구하였다.

'''
