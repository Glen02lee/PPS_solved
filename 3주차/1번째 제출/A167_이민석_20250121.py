#PPS "A167"
def solution(food):
    left = ''
    right = ''
    
    for i in range(1, len(food)):
        left += str(i) * (food[i] // 2) 
        right = str(i) * (food[i] // 2) + right 
    
    return left + '0' + right

'''
각 음식에 대해 양을 절반씩 나누어 배치한다
중앙에 물이 있다
오른쪽 선수에 경우에는 뒤에서부터 배치를 해주어야한다

'''