#PPS "A005"
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_order = ''.join(c for c in tree if c in skill)
        is_valid = True
        for i in range(len(skill_order)):
            if skill_order[i] != skill[i]:
                is_valid = False
                break
        if is_valid:
            answer += 1
    return answer

"""
이 문제또한 c언어 풀어봤던 문제라서 금방 풀수 있었다
파이썬을 통해 문제구현을 해보며 느끼는 것인데, 기본적으로 제공되는 문자열 처리 함수들이 많아서
코드가 간결해지는 것 같다.
"""