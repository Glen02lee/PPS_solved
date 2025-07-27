#PPS "A075"
def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 정렬: 두 문자열을 이어붙인 결과를 기준으로 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    result = ''.join(numbers)
    
    # 결과가 '0000...'인 경우, '0' 하나만 반환
    return '0' if result[0] == '0' else result