#PPS "A030"
num, mood = map(int, input().split())

arr = list(map(float, input().split()))

good, bad = 0, 0

if mood == 0:
    good = 1.0
else:
    bad = 1.0

for _ in range(num):
    happy = good * arr[0] + bad * arr[2]
    sad = good * arr[1] + bad * arr[3]
    good, bad = happy, sad

print(f"{good * 1000:.0f}")
print(f"{bad * 1000:.0f}")
"""
기분이 좋을 확률을 판단하는 함수
현재기분을 토대로 n일 후의 확률을 파악하는 것이므로,
good or bad 일때를 잘 구별하여 작성하면 큰 어려움이 없었던 것 같다.
"""