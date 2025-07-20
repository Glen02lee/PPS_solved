#PPS "A057"
def solution(cookie):
    n = len(cookie)
    max_val = 0

    for m in range(n - 1):
        left = m
        right = m + 1
        left_sum = cookie[left]
        right_sum = cookie[right]

        while left >= 0 and right < n:
            if left_sum == right_sum:
                max_val = max(max_val, left_sum)
            if left_sum <= right_sum and left > 0:
                left -= 1
                left_sum += cookie[left]
            elif right < n - 1:
                right += 1
                right_sum += cookie[right]
            else:
                break

    return max_val