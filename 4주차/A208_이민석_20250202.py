#PPS "A208"
import math

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def count_goldbach_partitions(n, primes):
    count = 0
    for i in range(2, n // 2 + 1):  # i와 n-i가 중복되지 않도록 n//2까지
        if primes[i] and primes[n - i]:
            count += 1
    return count

t = int(input())
max_n = 1000000  # 문제에서 주어진 n의 최대 범위, 필요에 맞게 설정
primes = sieve_of_eratosthenes(max_n)

for _ in range(t):
    n = int(input())
    print(count_goldbach_partitions(n, primes))
'''
math모듈을 사용하여 소수 판별을 위해 사용했다
제곱근을 통한 계산으로 빠르게 구현할 수 있게 하였다
에라토스테네스의 채를 이용한 문제를 이전에 풀었었는데 그부분을 응용하여 소수판별을 한번에 처리하였다
'''