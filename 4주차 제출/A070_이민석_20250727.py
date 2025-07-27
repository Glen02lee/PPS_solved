#PPS "A070"
from collections import deque

def last_card(N):
    queue = deque(range(1, N + 1))  # 1번부터 N번까지 큐에 넣기

    while len(queue) > 1:
        queue.popleft()          # 1. 제일 위 카드 버리기
        queue.append(queue.popleft())  # 2. 다음 카드 맨 뒤로 이동

    print(queue[0])  # 마지막 남은 카드 출력

# 입력 받기
N = int(input())
last_card(N)