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
