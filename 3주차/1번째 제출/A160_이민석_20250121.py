#PPS "A160"
def solution(n, m, section):
    section.sort()

    answer = 0
    current_end = 0
    for s in section:
        if s > current_end:
            answer += 1
            current_end = s + m - 1

    return answer
'''
먼저 오름차순으로 정렬해주고
최소 횟수를 세면서 롤러가 칠할 구역의 끝위치를 정해 각 구역을 처리하는 방식으로
코드를 구현하였다
만약 롤러가 현재구혁을 덮지 못하면 최대 범위 계산을 통해 답을 구한다

'''