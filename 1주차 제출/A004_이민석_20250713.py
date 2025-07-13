#PPS "A004"
def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    if not answer:
        return [-1]
    answer.sort()
    return answer

"""
C++로 풀어봤던 문제라서 금방 풀 수 있었다.
배열에서 특정 숫자로 나누어 떨어지는 수를 찾고, 없으면 -1을 반환하는 문제이다.
정렬도 필요하므로, 조건에 맞는 수를 찾은 후 정렬하여 반환한다.
"""