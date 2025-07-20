#PPS "A051"
def get_dial_time(word):
    dial_map = {
        3: "ABC", 4: "DEF", 5: "GHI", 6: "JKL",
        7: "MNO", 8: "PQRS", 9: "TUV", 10: "WXYZ"
    }
    
    time = 0
    for ch in word:
        for key, chars in dial_map.items():
            if ch in chars:
                time += key
                break
    return time

# 입력
word = input().strip().upper()
print(get_dial_time(word))