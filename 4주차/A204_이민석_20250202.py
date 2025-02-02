#PPS "A204"
n = int(input())
sum = 1
count = 0
for i in range(1, n + 1):
    sum *= i
while (sum > 0):
  if(sum % 10 != 0):
    break
  sum = sum // 10
  count += 1

print(count)

'''
팩토리얼을 구한후 0이 아닌수까지 반복문을 통해 구현하면 된다.
'''