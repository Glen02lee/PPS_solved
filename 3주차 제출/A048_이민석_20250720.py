#PPS "A048"
def is_group_word(word):
    seen = set()
    last_char = ''
    
    for ch in word:
        if ch != last_char:
            if ch in seen:
                return False
            seen.add(ch)
            last_char = ch
    return True

def main():
    n = int(input())
    count = 0
    for _ in range(n):
        word = input().strip()
        if is_group_word(word):
            count += 1
    print(count)

main()