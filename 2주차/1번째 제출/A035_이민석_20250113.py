#PPS "A035"
count = int(input())

for i in range(0, count):
  mars = list(map(str, input().split()))
  answer = float(mars[0])
  for j in range(len(mars)):      
    if mars[j] == "@":
      answer *= 3
    if mars[j] == "%":
      answer += 5
    if mars[j] == "#":
      answer -= 7

  print("{:.2f}".format(answer))
"""
조건에 맞게 @ % #을 구성해주고 문자열을 숫자로 바꿔주는 과정을
구현해주었다.
"""