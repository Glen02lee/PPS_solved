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
  


# @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자
# 소수점 두번째 자리까지 출력할 것 -> 정수가 아닌 실수 연산자로 받기
  
#1 문자열을 하나하나 봐주기 위해서는 반복문을 통해 볼 수 있다
#2 무슨 식이든 숫자가 먼저 오기 마련이다. 따라서 answer이라는 변수를 먼저 선언하면 된다.