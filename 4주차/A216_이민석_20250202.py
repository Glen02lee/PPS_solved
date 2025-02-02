#PPS "A216"
import sys

widths = { "0": 4, "1": 2 }  # 0과 1의 너비를 미리 저장
for i in range(2, 10):
    widths[str(i)] = 3  # 나머지 숫자는 3cm

while True:
    N = sys.stdin.readline().strip()
    if N == "0":
        break
    
    total_width = 2 + sum(widths[digit] for digit in N) + (len(N) - 1)
    print(total_width)
    
    '''
    sys.stdin.readline().strip()을 사용하여 한 줄씩 읽고, 0이 입력되면 종료시켰다
    너비 계산은
    1. 양쪽 경계 여백 2cm를 추가하고
    2. 숫자별 너비의 합을 구하고
    3. 숫자 사이에 여백 (길이 -1) cm를 추가해줬다
    '''
