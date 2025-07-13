#PPS "A016"
def solution(people, limit):
    people.sort()  # 몸무게를 오름차순 정렬
    left, right = 0, len(people) - 1  # 투 포인터 설정
    boats = 0  # 보트 개수

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람도 탑승 가능하면 태움
        right -= 1  # 가장 무거운 사람은 항상 태움
        boats += 1  # 보트 개수 증가

    return boats
