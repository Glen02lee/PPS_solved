#PPS "A068"
import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
queue = deque()
N = int(input())

for _ in range(N):
    cmd = input().strip()

    if cmd.startswith("push"):
        _, x = cmd.split()
        queue.append(int(x))

    elif cmd == "pop":
        print(queue.popleft() if queue else -1)

    elif cmd == "size":
        print(len(queue))

    elif cmd == "empty":
        print(0 if queue else 1)

    elif cmd == "front":
        print(queue[0] if queue else -1)

    elif cmd == "back":
        print(queue[-1] if queue else -1)