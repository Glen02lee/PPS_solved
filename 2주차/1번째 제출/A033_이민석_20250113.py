#PPS "A033"
arr = []
maxi = 0
maxn = 0

for i in range(5):
    total = 0
    row = list(map(int, input().split()))
    arr.append(row)
    total = sum(row)
    
    if maxn < total:
        maxn = total
        maxi = i

print(maxi + 1, maxn)
"""
각 줄의 합들을 구해 가장 큰 값을 구하는 문제
append와 sum을 이용하여 쉽게 구현하였다.
"""