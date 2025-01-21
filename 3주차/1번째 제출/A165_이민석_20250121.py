#PPS "A165"
def solution(number, limit, power):
    total_weight = 0
    
    for i in range(1, number + 1):
        divisors_count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisors_count += 1
                if j != i // j: 
                    divisors_count += 1
        
        if divisors_count > limit:
            total_weight += power
        else:
            total_weight += divisors_count
    
    return total_weight
'''
약수의 개수를 계산하여 그 개수에 따라 파워를 구하는문제이다
약수의 개수가 limit보다 크면, 그 숫자에 대해 power만큼 가중치를 더하고
그렇지 않으면 그 숫자의 약수의 개수만큼 가중치를 더한다
'''