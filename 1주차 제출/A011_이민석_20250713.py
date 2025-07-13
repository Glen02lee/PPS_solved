#PPS "A011"
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
