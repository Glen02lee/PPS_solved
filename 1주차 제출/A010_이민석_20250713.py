#PPS "A010"
def solution(s):
    len_s = len(s)
    min_length = len_s

    for step in range(1, len_s // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1

        for j in range(step, len_s, step):
            current = s[j:j + step]
            if prev == current:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)
                compressed += prev
                prev = current
                count = 1

        if count > 1:
            compressed += str(count)
        compressed += prev

        min_length = min(min_length, len(compressed))

    return min_length

