#PPS "A022"
num = int(input())
arr = list(map(int, input().split()))

y, m = 0, 0

for time in arr:
    y += (time // 30 + 1) * 10
    m += (time // 60 + 1) * 15

if y < m:
    print(f"Y {y}")
elif m < y:
    print(f"M {m}")
else:
    print(f"Y M {y}")

    """
    c로 이미 구현을 해봤던것이라 map()을 활용하여 입력문을 받는 것을 제외하고는
    비슷하게 구현을 해봤다.
    c에서는 동적할당을 위한 malloc을 사용하여 배열의 크기를 잡았었는데,
    파이썬은 이러한 작업이 불필요하기에 편한 느낌이 들었다.
    """