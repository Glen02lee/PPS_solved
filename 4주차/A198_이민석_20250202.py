#PPS "A198"
import sys
input = sys.stdin.readline

s, c = map(int, input().split())
L = [int(input()) for _ in range(s)]

start, end = 1, max(L)
resChick = 0

while start <= end:
    mid = (start + end) // 2
    
    cnt = sum(pa // mid for pa in L)
    
    if cnt >= c:
        resChick = max(resChick, mid)  
        start = mid + 1
    else:
        end = mid - 1 

res = sum(L) - (c * resChick)
print(res)

'''이진탐색을 통한 구현'''