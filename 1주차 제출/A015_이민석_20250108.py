size = 5
arr = list(map(int, input().split()))
result = sum(x ** 2 for x in arr) % 10
print(result)

"""
그냥 주어진 수를 제곱한 후 다 더한 후의 합을 10으로 나눈 나머지를 파악하면 된다
그식을 그대로 적었다
"""
