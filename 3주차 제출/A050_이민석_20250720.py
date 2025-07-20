#PPS "A050"
def decrypt_caesar(text):
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') - 3 + 26) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') - 3 + 26) % 26 + ord('a')))
        else:
            result.append(ch)  # 공백, 특수문자 등은 그대로 유지
    return ''.join(result)

# 입력받기
text = input()
print(decrypt_caesar(text))