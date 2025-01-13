#PPS "A029"
num = int(input())
first = int(input())

if num >= 6:
    print("Love is open door")
else:
    for i in range(1, num):
        if first == 0:
            print(i % 2)
        elif first == 1:
            print((i + 1) % 2)
    """
    이 문제도 C에서 구현하였을때는 long타입으로 지정하여 풍었었는데,
    큰 수가 자동적으로 변환되어 편했다.
    알고리즘은 문제에서 나온대로 구현하였다.
    """