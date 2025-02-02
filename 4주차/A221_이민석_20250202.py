#PPS "A221"
N = int(input())

for _ in range(N):
    K = input().strip()
    if K[-1] in '13579':  # 마지막 자리 숫자가 홀수인지 확인
        print("odd")
    else:
        print("even")
