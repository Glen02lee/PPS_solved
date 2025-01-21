#PPS "A162"
def solution(cards1, cards2, goal):
    i, j = 0, 0
    for word in goal:
        if i < len(cards1) and cards1[i] == word:  
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else: 
            return "No"
    
    return "Yes"

'''
순차적으로 카드1과 카드2에서 카드가 나와야한다

'''