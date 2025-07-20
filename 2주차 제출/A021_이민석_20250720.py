#PPS "A021"
import sys

num = int(sys.stdin.readline().strip())  # 첫 번째 입력 (num 값)

counts = list(map(int, sys.stdin.read().split()))[:num]  # 한 번에 모든 숫자 입력받고 num만큼 슬라이싱

sum_value = sum(counts) - (num - 1)  # (sum of counts) - (num - 1)

print(sum_value)
