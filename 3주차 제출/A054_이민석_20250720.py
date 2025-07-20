#PPS "A054"
def solution(board, moves):
    stack = []
    popped = 0

    # board는 행 기준으로 인형이 아래에 있는 구조이므로 열 기준으로 순회 필요
    n = len(board)

    for move in moves:
        col = move - 1  # 크레인은 1부터 시작하므로 인덱스 보정
        for row in range(n):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0

                if stack and stack[-1] == doll:
                    stack.pop()
                    popped += 2
                else:
                    stack.append(doll)
                break  # 해당 열에서 인형을 하나 뽑았으면 다음 move로

    return popped