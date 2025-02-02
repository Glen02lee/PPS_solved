#PPS "A209"
A, B = map(int, input().split())
m = int(input())
numbers = list(map(int, input().split()))

result = 0
for i in range(m):
    result += numbers[i] * (A ** (m - i - 1))

converted_numbers = []
while result > 0:
    converted_numbers.append(result % B)
    result //= B

converted_numbers.reverse()
for i in converted_numbers:
    print(i, end=' ')
    '''
    A진법 수를 10진수로 변환하고 각 자리에 해당하는 위치값을 정해주는 식을 적었다
    예를 들어, 첫 번째 자리이면 A^0, 두 번째 자리이면 A^1 이다
    그 두값을 곱하고 그 결과를 모두 더하여 10진수 값으로 변환하였다
    이후 이 10진수를 B진수로 다시 변환하였다
    '''