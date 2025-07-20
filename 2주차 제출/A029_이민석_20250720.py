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
