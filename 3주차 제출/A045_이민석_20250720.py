#PPS "A045"
def find_most_common_letter(word):
    letter_count = {}  # 알파벳 빈도수를 저장할 딕셔너리

    for letter in word:
        if letter.isalpha():  # 알파벳인 경우에만 처리
            letter = letter.upper()  # 대문자로 변환
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    max_count = 0  # 가장 많이 등장한 알파벳의 빈도수
    most_common_letters = []  # 가장 많이 등장한 알파벳들

    for letter, count in letter_count.items():
        if count > max_count:
            max_count = count
            most_common_letters = [letter]
        elif count == max_count:
            most_common_letters.append(letter)

    return most_common_letters

# 사용자 입력 받기
word = input().strip()

# 가장 많이 등장한 알파벳 찾기
most_common = find_most_common_letter(word)

# 결과 출력
if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])