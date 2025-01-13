#PPS "A021"

import sys

num = int(sys.stdin.readline().strip())

counts = list(map(int, sys.stdin.read().split()))[:num]

sum_value = sum(counts) - (num - 1)  # (sum of counts) - (num - 1)

print(sum_value)

"""
input()함수를 통해 구현할려고 하니 시간초과가 되어 찾아보니
sys를 사용하면 더욱 빠르게 입력을 받을 수 있다고 하여 sys를 사용하였다
아마도 대량입력이 된다면 시간제한 2초를 넘어가서 그렇게 되는 것 같다
문제구현자체는 굉장히 단순했다.
전체수에서 전체 개수의 합들에서 (플러그의 합-1)을 빼주면 된다.
"""