#PPS "A046"
def main():
    num = int(input())
    players = [input().strip() for _ in range(num)]
    
    arr = [0] * 26  # 알파벳 a~z에 해당하는 배열
    
    for name in players:
        first_char = name[0]
        arr[ord(first_char) - ord('a')] += 1

    result = ''
    for i in range(26):
        if arr[i] >= 5:
            result += chr(i + ord('a'))
    
    if result:
        print(result)
    else:
        print("PREDAJA")

main()