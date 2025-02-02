#PPS "A194"
num = int(input())
a = []
b = []
arr = []
for i in range(num):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    arr.append(x + y)
for i in range(num):
    print(f"Case #{i+1}: {a[i]} + {b[i]} = {arr[i]}") 