def solution(N, stages):
    failure_rates = []
    total_players = len(stages)  

    for stage in range(1, N + 1):
        not_cleared = stages.count(stage)  
        if total_players == 0:  
            failure_rate = 0
        else:
            failure_rate = not_cleared / total_players  

        failure_rates.append((failure_rate, stage))  
        total_players -= not_cleared  

    failure_rates.sort(key=lambda x: (-x[0], x[1]))  

    return [stage for _, stage in failure_rates]

    """
    각 스테이지 별로 도달했지만 클리어하지 못한 플레이어의 비율(실패율)을 계산하여, 실패율이 높은 순서대로 스테이지 번호를 정렬
    실패율은 (스테이지 도달->클리어 실패) / (해당 스테이지 도달자들의 합)
    실패율을 내림차순으로 정렬하되, 실패율이 같으면 스테이지 번호를 기준으로 오름차순 정렬이다.
    lambda 문법에 대해 익숙하지 않았는데, 이번기회에 사용해보았다.
    익명의 함수를 정의하기 위해 사용하고, 나는 실패율 정렬을 위해 사용하였다.
    """