#PPS "A163"
def solution(today, terms, privacies):
    answer = []
    
    today_year, today_month, today_day = map(int, today.split('.'))
    today_date = today_year * 12 * 28 + today_month * 28 + today_day
    
    term_dict = {}
    for term in terms:
        term_type, months = term.split()
        term_dict[term_type] = int(months)
    
    for i, privacy in enumerate(privacies):
        date_str, term_type = privacy.split()
        year, month, day = map(int, date_str.split('.'))
        
        privacy_date = year * 12 * 28 + month * 28 + day
        
        term_months = term_dict[term_type]
        privacy_date += term_months * 28
        
        if privacy_date <= today_date:
            answer.append(i + 1)
    return answer

'''
날짜형태를 yyyymmdd형태로 변환해주고
약관에 대한 유효기간 정보를 딕셔너리로 저장했다
이전 문제였던 순위 바꾸기에서 사용했던 방식대로 딕셔너리를 만들어서 매핑해주었다
이후에는 유효기간을 확인하며 파기해야할 개인정보를 지우는 식으로 구현하였다
'''
