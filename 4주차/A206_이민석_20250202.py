#PPS "A206"
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 첫 번째 동생과의 차이로 GCD를 초기화
d = abs(s - a[0])

# 나머지 동생들과의 차이에 대해 GCD 계산
for i in range(1, n):
    d = gcd(d, abs(s - a[i]))

print(d)
'''
처음에는 min()을 사용하여 최솟값을 찾았는데
문제에서 요구하는것은 최댓값을 찾아야했다
문제를 꼼꼼히 읽어야겠다..
'''