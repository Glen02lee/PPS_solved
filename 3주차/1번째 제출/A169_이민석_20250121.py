#PPS "A169"
def solution(ingredient):
    answer = 0
    stack = [] 
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1 
            stack.pop()  
            stack.pop()  
            stack.pop()  
            stack.pop()
    
    return answer

'''
햄버거를 만드는것이므로 직관적으로 스택을 떠올렸다
위에서부터 뺀다고 생각하면서 햄버거의 재료들을 직관적으로 표현하고 싶었다
처음에는 스택의 슬라이싱 기능을 사용하여 문제를 제출하였다
stack = stack[:-4]  형태로 슬라이싱을 구현하다보니 시간오류가 계속 나게 되었다
그래서 조금더 효율적인 방법으로  pop을 사용하였다.
'''