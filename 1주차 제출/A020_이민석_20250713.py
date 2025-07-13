#PPS "A020"
total, max_people = 0, 0

for _ in range(4):
    a, b = map(int, input().split())
    total += -a + b
    max_people = max(max_people, total)

print(max_people)
