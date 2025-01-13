#PPS "A034"
arr = []
count = 0

for i in range(10):
    num = int(input())
    arr.append(num % 42)

for i in range(10):
    for j in range(i+1, 10):
        if arr[i] == arr[j]:
            count += 1
            break

print(10 - count)
"""
수 10개를 입력받아 42로 나눈 후 서로 다른 수가 몇개인지 알아내는 수
따라서 배열을 선언하여 10개를 받은 후 42로 나눈값을 저장했고
그 값들끼리 같은 값이 있는지 파악하는 count를 사용하여 10- count를 통해 구현하였다.


**코드 재구성**
arr = {int(input()) % 42 for _ in range(10)}
print(len(arr))

이렇게도 구현이 가능 할 것 같다.
{}을 통해 set을 사용하는 방식인데, set은자동적으로 중복된 값들을 지워주기 때문에
입력을 받고 42로 나눈값들을 set에 넣을때 중복체크를 위한 반복문이 필요없을것이다.
"""