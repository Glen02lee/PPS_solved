#PPS "A066"
def main():
    num = input()  # 문자열로 입력 받기

    # 내림차순 정렬: 문자열을 리스트로 바꾸고 정렬
    sorted_num = ''.join(sorted(num, reverse=True))

    print(sorted_num)

if __name__ == "__main__":
    main()