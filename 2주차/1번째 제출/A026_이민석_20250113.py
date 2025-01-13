#PPS "A026"
def solution(x):
    digit_sum = sum(int(digit) for digit in str(x))
    return x % digit_sum == 0

    """
    하샤드 수란 주어진 숫자가 그 자릿수의 합으로 나누어떨어지는 것을 말한다.
    이를 판별하기 위한 함수이므로 불리언타입으로 리턴되도록 했다.
    digit_sum = sum(int(digit) for digit in str(x))와 같은 형태로 구현을 해보았는데,
    문자열로 반환된 x에서 각 문자를 하나씩 순차적으로 가져와 더하는 방식을 구현하고 싶었는데
    뭔가 파이썬에서 이런 기능을 할법한 문법을 만들었을 것 같아 찾아보게 되었고 사용하였다.
    """