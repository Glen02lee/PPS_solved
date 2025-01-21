#PPS "A170"
def solution(a, b, n):
    answer = 0
    while n >= a: 
        cola = (n // a) * b 
        n = (n % a) + cola 
        answer += cola 
    
    return answer

'''
빈볃이 a개 이상일때는 교환이 가능하다
각 식을 넣고 구현하니 금방 구현이 되었다.
'''