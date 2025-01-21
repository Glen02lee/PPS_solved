#PPS "A157"
def can_install_routers(houses, c, distance): 
    count = 1  # 첫 번째 집
    last_installed = houses[0]  # 마지막 집

    for house in houses[1:]:
        if house - last_installed >= distance:  # 최소 거리 조건 충족 시
            count += 1
            last_installed = house 

            if count >= c:
                return True

    return False

def find_max_distance(houses, c):
    houses.sort() # 집 좌표에 따른 정렬
    left, right = 1, houses[-1] - houses[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_install_routers(houses, c, mid):
            result = mid 
            left = mid + 1 
        else:
            right = mid - 1 

    return result

n, c = map(int, input().split()) 
houses = [int(input()) for _ in range(n)]

print(find_max_distance(houses, c))
'''
이 문제도 이진탐색을 활용하여 해결할 수 있다고 생각했다
가능한 최소 거리는 1이 되고, 최대 거리는 가장 먼 두 집 사이의 거리이다
이 부분을 보고 중간 값으로 잘라 범위 내 최소거리와 최대 거리를 구할 수 있다고 생각했다
첫 함수는 주어진 거리로 라우터를 설치할 수 있는지 확인하고
다른 함수는 이진 탐색을 통해 최대 최소 거리를 찾는 것이다

코드를 깔끔하게 하기 위해 두개의 동작을 하는 함수로 구분지어 구현하였다.
'''