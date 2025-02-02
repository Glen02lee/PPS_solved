#PPS "A218"
T = int(input())
for _ in range(T):
    c, v = map(int, input().split())
    if c % v == 0:
        print("You get {} piece(s) and your dad gets {} piece(s).".format(c // v, 0))
    else:
        print("You get {} piece(s) and your dad gets {} piece(s).".format(c // v, c % v))
'''
출력문의 format을 사용해서 쉽게 구현할 수 있었다
'''