#PPS "A006"
def solution(s):
    answer = True
    p = 0
    y = 0
    
    for c in s:
        c = c.lower()
        if c == 'p':
            p += 1
        if c == 'y':
            y += 1
    
    if p != y:
        answer = False
    
    return answer