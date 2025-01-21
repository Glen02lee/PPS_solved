#PPS "A168"
def solution(k, m, score):
    score.sort(reverse=True)
    
    total_profit = 0
    
    for i in range(0, len(score) // m * m, m):
        total_profit += score[i + m - 1] * m
    
    return total_profit

'''
최대이익을 내야하므로 가장 높은 점수의 사과를 묶어서 파는 것이 유리하므로
내림차순 정렬을 해주었다
상자를 만들 수 있는 개수는 score의 길이를 m으로 나눈 몫이된다.

'''