#PPS "A161"
def solution(keymap, targets):
    keypress = {}
    for i, key in enumerate(keymap):
        for j, char in enumerate(key):
            if char not in keypress:
                keypress[char] = j + 1
            else:
                keypress[char] = min(keypress[char], j + 1)  
    result = []
    for target in targets:
        total_presses = 0
        for char in target:
            if char in keypress:
                total_presses += keypress[char]
            else:
                total_presses = -1
                break
        result.append(total_presses)

    return result
'''
각문자에 대해 최소 횟수를 계산하고
각 목표 문자열에 대해 최소 횟수를 계산하면 된다고 생각했다
'''
