#PPS "A032"
def calculate_residents(k, n):
    residents = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        residents[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            residents[i][j] = residents[i][j - 1] + residents[i - 1][j]

    return residents[k][n]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(calculate_residents(k, n))
    """
    처음에 구현할때에는 residents[i][j] = sum(residents[i - 1][1:j + 1])이런식으로 구현하였는데
    이전 방의 거주자 수를 이용할 수 있기때문에 중복 계산을 피하기 위해 코드를 교체해보았다.
    sum을 이용하여 쉽게 구현할 수 있었다.
    """