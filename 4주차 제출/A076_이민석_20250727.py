#PPS "A076"
scores = [int(input()) for _ in range(8)]

# 각 점수를 (점수, 문제번호) 쌍으로 묶기 (문제번호는 1부터 시작)
indexed = [(score, idx + 1) for idx, score in enumerate(scores)]

# 점수를 기준으로 내림차순 정렬 후, 상위 5개 선택
top5 = sorted(indexed, reverse=True)[:5]

# 총점 계산
total_score = sum(score for score, _ in top5)

# 해당 문제 번호만 추출해서 오름차순 정렬
selected_problems = sorted(idx for _, idx in top5)

# 결과 출력
print(total_score)
print(' '.join(map(str, selected_problems)))