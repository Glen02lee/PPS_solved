#PPS "A215"
import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    total = 0

    for _ in range(N):
        total += int(sys.stdin.readline())

    if total > 0:
        print("+")
    elif total < 0:
        print("-")
    else:
        print("0")

        '''
        입력 최적화를 위한 sys를 사용하고 반복문을 통해 합계 누적을 했다
        '''