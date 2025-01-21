#PPS "A159"
def solution(wallpaper):
    min_row = float('inf')
    min_col = float('inf')
    max_row = -float('inf')
    max_col = -float('inf')
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    
    # 결과 반환
    return [min_row, min_col, max_row + 1, max_col + 1]

'''
조금 더 깔끔하게 풀 수 있을 수 있겠지만
가장 먼저 생각난 풀이 방법이었다
가장 직관적으로 해결할 수 있었다
물론 두개의 배열을 임의로 선언하여
이중 반복문으로 append할 수 있겠지만 조금더 직관적으로 풀고 싶었다

'''