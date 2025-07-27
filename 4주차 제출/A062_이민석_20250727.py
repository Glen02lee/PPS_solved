#PPS "A062"
import datetime

def solution(a, b):
    day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    date = datetime.date(2016, a, b)
    return day_list[date.weekday()]