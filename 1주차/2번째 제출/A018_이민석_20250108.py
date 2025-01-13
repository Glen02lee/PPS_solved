#PPS "A018"
def min_scalar_product(num, a_arr, b_arr):
    a_arr.sort()       # 오름차순 정렬
    b_arr.sort(reverse=True)  # 내림차순 정렬

    return sum(a * b for a, b in zip(a_arr, b_arr))

num = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

print(min_scalar_product(num, a_arr, b_arr))

"""
최소 스카라 곱을 구하는 문제라고 생각했다.
주어진 두 배열에 대해 오름차순, 내림차순 정렬을 한 후 
zip문법을 통해 배열을 짝지어준다.
그렇게 된다면 가장 큰 값과 가장 작은 값들을 곱한 결과를 출력할 수 있게 된다.
"""