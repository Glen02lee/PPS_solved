#PPS "A065"
# 좌표를 담는 Point 클래스 정의 (선택사항: 꼭 안 써도 됨)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} {self.y}"

def main():
    N = int(input())
    points = []

    # 좌표 입력 받기
    for _ in range(N):
        x, y = map(int, input().split())
        points.append(Point(x, y))

    # 정렬: x 기준 오름차순, x가 같으면 y 기준 오름차순
    points.sort(key=lambda p: (p.x, p.y))

    # 결과 출력
    for point in points:
        print(point)

if __name__ == "__main__":
    main()