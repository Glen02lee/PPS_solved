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
