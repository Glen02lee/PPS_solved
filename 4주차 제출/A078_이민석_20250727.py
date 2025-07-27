#PPS "A078"
def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # 가장 큰 h를 찾기 위한 반복
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i
    return len(citations)