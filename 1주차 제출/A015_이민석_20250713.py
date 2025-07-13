#PPS "A015"
size = 5
arr = list(map(int, input().split()))  # 한 줄에 입력받음
result = sum(x ** 2 for x in arr) % 10
print(result)
"""
    연속된 숫자 범위를 파악한 후 이를 요약하는 문제이다
    연속된 숫자가 있다면 화살표 ->를 이용해서 시작점과 끝을 알려주는 것인데,
    반복문을 통해 간단히 구현해보았다.
    f"{}" 문법을 통해 배열에 추가하는 방식대로 구현했다.
       
       
"""
