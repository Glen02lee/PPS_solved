#PPS "A205"
def count_trailing_zeros(n, m):
    def count_factors(n, factor):
        count = 0
        while n >= factor:
            count += n // factor
            n //= factor
        return count

    count_5_n = count_factors(n, 5)
    count_5_m = count_factors(m, 5)
    count_5_nm = count_factors(n - m, 5)
    
    count_2_n = count_factors(n, 2)
    count_2_m = count_factors(m, 2)
    count_2_nm = count_factors(n - m, 2)

    count_5 = count_5_n - (count_5_m + count_5_nm)
    count_2 = count_2_n - (count_2_m + count_2_nm)

    return min(count_2, count_5)

n, m = map(int, input().split())
print(count_trailing_zeros(n, m))

'''
난 처음에 5의 거듭제곱만 고려했는데, 끝자리 0을 만드는 요인이 2의 거듭제곱도 있기때문에
오류가 났었다
5와 2의 개수를 모두 고려해야하므로
조합 nCm = n! / (m! * (n-m)!)에서 끝자리 0의 개수는 
n!, m!, (n-m)!에서 나오는 2와 5의 개수를 바탕으로 계산하면 된다
'''
