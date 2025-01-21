#PPS "A158"
def solution(players, callings):
    rank_map = {name: i for i, name in enumerate(players)}

    for name in callings:
        current_rank = rank_map[name]
        
        if current_rank == 0:
            continue

        previous_player = players[current_rank - 1]

        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]

        rank_map[name] -= 1
        rank_map[previous_player] += 1

    return players

'''
선수들의 순위를 바꾸는 문제
처음에는 매핑이 익숙치 않아 떠오르지 않았는데, 다 푼 이후 다른 사람들의 코드를 봤는데
매핑을 통하여 선수이름을 키로, 순위를 인덱스로 매핑하여 딕셔너리를 만든것을 봤다
이 딕셔너리를 통해 리스트에 있는 각 선숭이름에 대해 순위를 변경하고
최종적으로 업데이트된 리스트를 반환해준다

'''