#PPS "A027"
def solution(number, k):
    stack = []
    
    for digit in number:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    return ''.join(stack[:len(number) - k])
    """
    스택 자료구조를 이용해서 만든 숫자의 조합이 클때는 쌓고 작을떄는 제거하는 방식으로 구현해봤다.
    스택을 반복문안에서 처리할때 c와는 문법적으로 다르게 접근한다는 생각이 들었다.
    스택은 리스트로 구현되어있으며, 마지막 요소와 계속해서 넣고자하는 수를 비교하는 방식이다.
    마지막 리턴값은 문제가 요구하는 출력형태로 나타내기 위해 join()을 사용하였다.
    """