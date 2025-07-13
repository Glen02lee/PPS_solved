#PPS "A007"
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

mixed = list(map(int, input().split()))

if mixed == ascending:
    print("ascending")
elif mixed == descending:
    print("descending")
else:
    print("mixed")