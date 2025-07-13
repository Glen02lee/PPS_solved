#PPS "A017"
def min_sets_needed(num: str) -> int:
    count = [0] * 10

    for digit in num:
        count[int(digit)] += 1

    sn = count[6] + count[9]
    sets = (sn + 1) // 2

    max_count = max(count[i] for i in range(10) if i != 6 and i != 9)

    return max(sets, max_count)

num = input()
print(min_sets_needed(num))


"""
방번호를 만들기 위해 필요한 숫자 세트의 개수를 구해야한다.
6과 9를 뒤집어서 사용할 수 있기 때문에 이를 하나로 생각하면 된다고 생각했다
따라서 각 숫자별로 카운트를 하고 6과 9는 하나로 생각하기때문에 둘이 합친 후 세트가 필요하기 때문에
// 2를 해준다
"""
