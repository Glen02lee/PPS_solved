#PPS "A166"
def solution(t, p):
    answer = 0
    len_p = len(p)
    p_int = int(p)
    
    for i in range(len(t) - len_p + 1):
        substring = int(t[i:i + len_p])
        
        if substring <= p_int:
            answer += 1
    
    return answer

'''
p를 숫자로 변환해두어야 계산하기 편하다
t에서 p의 길이만큼 부분 문자열을 추출하고
그 이후의 숫자로 변환해준다
부분 문자열이 p보다 작거나 같으면 카운트를 계속 증가하여 반환해준다

'''