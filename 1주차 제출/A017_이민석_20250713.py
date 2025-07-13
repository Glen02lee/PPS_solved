#PPS "A017"
def min_sets_needed(num: str) -> int:
    count = [0] * 10

    for digit in num:
        count[int(digit)] += 1

    sn = count[6] + count[9]
    sets = (sn + 1) // 2  # 6과 9를 공유할 수 있는 세트 계산

    max_count = max(count[i] for i in range(10) if i != 6 and i != 9)

    return max(sets, max_count)

num = input()
print(min_sets_needed(num))
"""
    이 문제는 주어진 숫자 문자열에서 각 숫자의 개수를 세고,
    6과 9는 함께 묶어서 처리하는 방식으로 최소 세트의 개수를 계산하는 문제이다.
    각 숫자의 개수를 세기 위해 리스트를 사용하고, 6과 9의 개수는 합쳐서 처리한다.
    최종적으로 가장 많이 등장한 숫자의 개수와 6, 9의 세트를 비교하여 최대값을 반환한다.
"""