#PPS "A164"
def solution(s):
    answer = []
    last_seen = {} 
    
    for i, char in enumerate(s):
        if char in last_seen:
            answer.append(i - last_seen[char])
        else:
            answer.append(-1)
        last_seen[char] = i
    
    return answer

'''
각 문자에 대해 마지막으로 나온 위치를 저장할 딕셔너리를 만들어 주었다

이전에 나온 문자면 그 위치를 저장하고,
처음 나온 문자라면 -1을 저장했다
'''