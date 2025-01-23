#PPS "B014"
import sys
from collections import deque

input = sys.stdin.read

def count_islands(map_data, w, h):
    # 8방향 (상, 하, 좌, 우, 대각선)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    visited = [[False] * w for _ in range(h)]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        while queue:
            cx, cy = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and map_data[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    island_count = 0
    for i in range(h):
        for j in range(w):
            if map_data[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                island_count += 1
                
    return island_count

data = input().strip().split("\n")
result = []
i = 0

while i < len(data):
    w, h = map(int, data[i].split())
    if w == 0 and h == 0:
        break
    
    map_data = []
    for j in range(h):
        map_data.append(list(map(int, data[i + 1 + j].split())))
    
    result.append(count_islands(map_data, w, h))
    i += h + 1

sys.stdout.write("\n".join(map(str, result)) + "\n")

'''
대각선이 포함된 8개의 방향 모두 고려를 해야 풀리는 문제였다
'''