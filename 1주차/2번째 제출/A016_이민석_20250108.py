def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats

"""
몸무게를 오름차순으로 정렬해주고
왼쪽, 오른쪽 두개의 지점을 설정해준다.
가장 무거운 사람은 항상 태우고, 
그 이후 가장 가벼운사람을 태웠을때 탑승이 가능하면 태우는 식으로 생각했다.
"""
