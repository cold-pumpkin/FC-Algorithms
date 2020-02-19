# 1023. 유기농 배추
import sys
sys.setrecursionlimit(10000)

T = int(input())
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 벌레 탐색 : 상하좌우 모든 경우를 끝까지 이동하면서 0으로 셋팅
def move(field, check, r, c):
    if check[r][c]:
        return
    check[r][c] = 1
    for k in range(4):
        rr = r + dr[k]
        cc = c + dc[k]
        # 배추가 존재하지 않거나 방문하지 않은 경우에만 호출
        if field[rr][cc] == 0 or check[rr][cc]:
            continue
        move(field, check, rr, cc)

def process():
    M, N, K = map(int, input().split()) # 가로길이(열 개수), 세로길이(행 개수), 배추 개수

    ans = 0
    field = [[0] * (M+2) for _ in range(N+2)]  # 배추밭 (가상의 0의 테두리 추가)
    check = [[0] * (M+2) for _ in range(N+2)]  # 방문여부 (DFS 재귀호출 최소화를 위해 추가)
    
    # 배추 위치를 받아 1로 셋팅
    for j in range(K):
        y, x = map(int, input().split())  # 가로 위치, 세로 위치
        field[x+1][y+1] = 1
    
    # 배추가 존재하면 벌레 이동 탐색
    for n in range(1, N+1):  # 행
        for m in range(1, M+1):  # 열
            if field[n][m] == 0 or check[n][m]:
                continue
            move(field, check, n, m)
            ans += 1
    
    print(ans)

for i in range(T):
    process()
    