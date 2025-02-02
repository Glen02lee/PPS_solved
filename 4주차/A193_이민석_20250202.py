#PPS "A193"
N = int(input())  # 입력 받기

# N이 주어지면, long의 개수는 N // 4 입니다.
num_of_longs = N // 4

# "long"을 num_of_longs 번 붙여서 정수 자료형을 생성
result = "long " * (num_of_longs - 1) + "long int"

# 결과 출력
print(result)
