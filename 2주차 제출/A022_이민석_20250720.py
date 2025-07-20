#PPS "A022"
num = int(input())
arr = list(map(int, input().split()))

y, m = 0, 0

for time in arr:
    y += (time // 30 + 1) * 10
    m += (time // 60 + 1) * 15

if y < m:
    print(f"Y {y}")
elif m < y:
    print(f"M {m}")
else:
    print(f"Y M {y}")
