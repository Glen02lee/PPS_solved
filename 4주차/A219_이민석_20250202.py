#PPS "A219"
import math

D, H, W = map(int, input().split())

x = D / math.sqrt(H**2 + W**2)

# 실제 높이와 너비 계산 (소수점 이하 버림)
height = int(H * x)
width = int(W * x)

print(height, width)
