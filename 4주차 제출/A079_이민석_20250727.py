#PPS "A079"
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced = array[i-1:j]        # i번째부터 j번째까지 자르기 (i-1 ~ j-1 인덱스)
        sorted_slice = sorted(sliced)  # 오름차순 정렬
        answer.append(sorted_slice[k-1])  # k번째 수 추출 (k-1 인덱스)
    return answer