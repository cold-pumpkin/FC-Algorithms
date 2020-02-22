# 12100. 2048(Easy)

# 이동 후 맵을 출력하는 것이 아니라, 최대값만 출력하기 때문에
# 한가지 방향으로 음직이는 경우만 구현하고 (ex. 전체 왼쪽 슬라이딩)
# 맵 자체를 90도씩 돌려주어 이동시키는 방식을 적용

from copy import deepcopy

N = int(input())
Game = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]  # 상하좌우

# 왼쪽으로 하나의 행을 슬라이드
def slide(row, N):
    newRow = [r for r in row if r]  # 양수인 것만 리턴
    for i in range(1, len(newRow)):
        # ex. [2, 2, 2, 2] -> [4, 0, 4, 0]
        if newRow[i-1] == newRow[i]:
            newRow[i-1] *= 2
            newRow[i] = 0
    newRow = [r for r in newRow if r]  # 다시 양수인 것만 리턴 (ex. [4, 0, 4, 0] -> [4, 4])
    return newRow + [0] * (N-len(newRow))  # 부족한 자리는 0으로 채워서 리턴


# 게임판 전체를 시계방향 90도 돌리기 (외우기)
def rotate90(N, G):  
    newG = deepcopy(G)
    for i in range(N):
        for j in range(N):
            newG[j][N-i-1] = G[i][j]  # 1행 -> 마지막 열 / 2행 -> 마지막-1열 ...
    return newG

def move(N, G, count):
    ret = max([max(g) for g in G])
    if count == 0:  # 5번 모두 이동시킨 경우
        return ret
    
    # 게임판을 4개 방향으로 돌려가며 슬라이딩 적용
    for _ in range(4):
        tmpG = [slide(g, N) for g in G]  # 한 쪽 방향으로 행마다 슬라이딩
        if tmpG != G:
            ret = max(ret, move(N, tmpG, count-1))
        G = rotate90(N, G)  # 게임판을 90도 돌리기

    return ret 

print(move(N, Game, 5))
