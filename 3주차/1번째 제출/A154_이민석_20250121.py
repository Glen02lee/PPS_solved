#PPS "A154"
def calculate_min_cost(n, distances, prices):
    min_cost = 0
    min_price = prices[0]  # 첫 도시에서의 기름값
    
    for i in range(n - 1):
        min_cost += min_price * distances[i]  #최소 거리
        if prices[i + 1] < min_price: 
            min_price = prices[i + 1]
    
    return min_cost

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split())) 

print(calculate_min_cost(n, distances, prices))
'''
그리디 알고리즘을 이용해야한다고 생각했다.
이 문제에서는 항상 적은 기름값을 그 순간마다 계산을 해야하기 때문이다
여러 도시를 지나가면서 기름을 살 때 최소 비용으로 목적지에 도착해야하는데,
기름값이 적은 곳에서 많이 사야하고 이동할 거리가 짧은 곳에서는 기름값이 더 비싸도 상관이 없다

다시 말해 현재 위치에서의 기름값과 이후 위치에서의 기름값을 비교하여
가장 저렴한 기름값으로 미리 기름을 사는 방식으로 해결해야한다
'''