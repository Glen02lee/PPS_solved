#PPS "A201"
def reverse_words(S):
    result, current_word, in_tag = [], "", False
    for char in S:
        if char == '<': 
            in_tag = True
            if current_word:
                result.append(current_word[::-1])
                current_word = ""
            result.append(char)
        elif char == '>':
            in_tag = False
            result.append(char)
        elif char == ' ' and not in_tag:
            result.append(current_word[::-1])
            result.append(' ')
            current_word = ""
        else:
            if in_tag:
                result.append(char)
            else:
                current_word += char
    if current_word:
        result.append(current_word[::-1])
    return ''.join(result)

S = input()
print(reverse_words(S))
'''
문자를 한 글자씩 확인하면서 내용은 그대로 두고, 그외의 단어들은 뒤집어서 결과에 추가해야했다
그냥 단순히 뒤집는것이 아니라 그 단어의 위치는 그대로 둔 상태에서 뒤집어야했기 때문이다
'''
