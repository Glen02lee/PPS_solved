#PPS "A197"
n, m = map(int, input().split())
num = list(range(1, n+1))

for _ in range(m):
  a, b = map(int, input().split())
  num[a-1], num[b-1] = num[b-1], num[a-1]

print(*num)