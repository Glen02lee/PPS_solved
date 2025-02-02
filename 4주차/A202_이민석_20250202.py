#PPS "A202"
import sys
from collections import deque

n = int(sys.stdin.readline())
postfix = sys.stdin.readline().strip()
values = [int(sys.stdin.readline()) for _ in range(n)]

stack = deque()

for char in postfix:
    if char.isalpha():
        stack.append(values[ord(char) - ord('A')])
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if char == '+':
            stack.append(operand1 + operand2)
        elif char == '-':
            stack.append(operand1 - operand2)
        elif char == '*':
            stack.append(operand1 * operand2)
        elif char == '/':
            stack.append(operand1 / operand2)

print(f"{stack.pop():.2f}")
'''
스택을 사용하여 연산 중간 결과들을 계속해서 저장하게 했다
postfix 문자열을 한 문자씩 처리한다
문자가 알파벳일 경우 A부터 Z까지의 알파벳은 각 피연산자에 대응하므로,
해당 알파벳에 해당하는 값을 values 리스트에서 찾아 스택에 추가한다
ord(char) - ord('A')을 통해 알파벳을 인덱스로 변환하였다
연산자일 경우 두 개의 피연산자를 스택에서 꺼낸 후
해당 연산자에 맞는 계산을 하고, 결과를 다시 스택에 넣는다
후위 표기법에서 연산자는 항상 피연산자 뒤에 나온다
연산 시 첫 번째로 꺼낸 값은 두 번째 피연산자(operand2)이고, 
두 번째로 꺼낸 값은 첫 번째 피연산자(operand1)가 된다
'''