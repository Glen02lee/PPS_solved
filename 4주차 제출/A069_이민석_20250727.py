#PPS "A069"
from collections import deque

def josephus(N, K):
    people = deque(range(1, N + 1))  # 1번부터 N번까지 사람
    result = []

    while people:
        people.rotate(-(K - 1))  # 앞에서 K번째 사람이 앞으로 오도록 회전
        result.append(people.popleft())  # 제거된 사람 기록

    # 결과 형식 출력
    print(f"<{', '.join(map(str, result))}>")

# 입력 예시
N, K = map(int, input().split())
josephus(N, K)