#PPS "A018"
def min_scalar_product(num, a_arr, b_arr):
    a_arr.sort()       # 오름차순 정렬
    b_arr.sort(reverse=True)  # 내림차순 정렬

    return sum(a * b for a, b in zip(a_arr, b_arr))

num = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

print(min_scalar_product(num, a_arr, b_arr))
