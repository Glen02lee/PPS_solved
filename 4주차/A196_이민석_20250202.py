#PPS "A196"
n = int(input())
num = list(map(int, input().split()))
v = int(input())
count = 0
for i in range(n):
  if num[i] == v:
    count += 1
print(count)