#PPS "A047"
def main():
    s = input().strip()
    for i in range(len(s)):
        print(s[i], end='')
        if i % 10 == 9:
            print()
    # 마지막 줄에 줄바꿈이 없으면 알아서 처리해주는 것도 고려 가능

main()