#PPS "A052"
def calculate_score(results):
    scores = []
    for result in results:
        count = 0
        streak = 0
        for ch in result:
            if ch == 'O':
                streak += 1
                count += streak
            else:
                streak = 0
        scores.append(count)
    return scores

# 입력 처리
num = int(input())
results = [input().strip() for _ in range(num)]

# 점수 계산 및 출력
for score in calculate_score(results):
    print(score)