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
