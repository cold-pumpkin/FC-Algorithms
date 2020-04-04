# 1012. 유기농 배추
# BFS / DFS - 연결요소(상하좌우) 개수 세기

import sys
sys.setrecursionlimit(10000)

# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    # 상하좌우 인접한 모든 배추 위치 탐색
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 범위 벗어난 경우 skip
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 배추인 경우 재귀호출
        if grid[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(int(input())):
    M, N, K = map(int, input().split())  # 가로, 세로, 배추개수
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 배추 위처 정보 입력
    for _ in range(K):
        b, a = map(int, input().split())  # 열, 행
        grid[a][b] = 1
    
    answer = 0
    for i in range(N):
        for j in range(M):
            # 배추가 존재하고, 처음 방문한 경우 경우 DFS 수행
            if grid[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)

