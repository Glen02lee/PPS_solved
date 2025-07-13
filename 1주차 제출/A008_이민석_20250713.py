#PPS "A008"
sn = int(input())
score = []
over_avg = []

for i in range(sn):
    n, *scores = map(int, input().split())
    score.append(scores)
    sum_scores = sum(scores)
    avg = sum_scores / n
    count = sum(1 for s in scores if s > avg)
    over_avg.append(count / n * 100)

for percentage in over_avg:
    print(f"{percentage:.3f}%")