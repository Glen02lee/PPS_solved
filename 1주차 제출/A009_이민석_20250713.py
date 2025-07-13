#PPS "A009"
def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    
    for c in s:
        if not c.isdigit():
            answer = False
    
    return answer

