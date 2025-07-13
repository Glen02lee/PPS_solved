#PPS "A020"
total, max_people = 0, 0

for _ in range(4):
    a, b = map(int, input().split())
    total += -a + b
    max_people = max(max_people, total)

print(max_people)

"""
4번의 입력 중 각 구간에서 탑승한 사람수와 하차한 사람수를 파악해서
가장 많을때를 구하는 것이다.
a는 하차이므로, 계속 빼주고, b는 승차이므로 계속 더해준다
그때마다 최댓값이바뀌면 그값을 바뀌도록 구현하였다.
"""