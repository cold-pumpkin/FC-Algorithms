# 16768. Mooyo Mooyo

N, K = map(int, input().split())
H = [list(map(int, input())) for _ in range(N)]

#print(H)

# 변화가 존재하는한 위 과정 계속 반복
# 전체 탐색하면서 1 이상인 수를 찾으면 탐색 시작
# H와 같은 크기의 check 리스트 생성, 초기화 (같은 그룹인지 체크)
# 같은 숫자의 그룹 찾기
#  - 4개 방향으로 탐색하며 같은 숫자이면 check를 True로 셋팅, 리턴값+1 .. (1)
# 리턴값이 K개 이상이면 check가 True인 칸을 모두 0으로 셋팅 .. (2)
# H를 끝까지 한 번 탐색했으면 모두 아래로 떨어뜨리기 .. (3)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 1) 인접한 같은 숫자 그룹 찾아 개수를 리턴
def search(x, y):
    check1[x][y] = True
    ret = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if check1[xx][yy] or H[x][y] != H[xx][yy]:
            continue
        ret += search(xx, yy)
    return ret

# 2) 같은 그룹인 숫자들을 모두 0으로 만들기
def makeZero(x, y, val):
    check2[x][y] = True
    H[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if check2[xx][yy] or H[xx][yy] != val:
            continue
        makeZero(xx, yy, val)
                
# 3) 0자리 채우기
def drop():
    # 각 열마다 가장 아래 요소부터 0이면 위 요소와 스위치
    for c in range(10):  # 열 
        for r in range(N-1, 0, -1):  # 행
            if H[r][c] == 0:
                H[r][c], H[r-1][c] = H[r-1][c], H[r][c]


while True:
    isChanged = False
    check1 = [[False] * 10 for _ in range(N)]  # 같은 그룹임을 체크 (True이면 다시 탐색하기 않음)
    check2 = [[False] * 10 for _ in range(N)]  # 삭제가 가능한지 체크
    # 전체 탐색
    for i in range(N):
        for j in range(10):
            if H[i][j] == 0 or check1[i][j]:
                continue
            res = search(i, j)  # 1) 인접한 같은 숫자 그룹 찾기
            if res >= K:
                makeZero(i, j, H[i][j])  # 2) 0으로 만들기
                isChanged = True
    if not isChanged:
        break
    for _ in range(N-1):
        drop()  # 3) 0자리 채우기


for h in H:
    print(''.join(list(map(str, h))))