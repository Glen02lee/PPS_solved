#PPS "A199"
n = int(input())

for i in range(n):
    if i % 2 == 1:
      print(n*" *")
    elif i % 2 == 0:
      print(n*"* ")   