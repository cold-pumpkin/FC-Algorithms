# 17406. 배열 돌리기 4

from copy import deepcopy

N, M, K = map(int, input().split())  # 행 수, 열 수, 회전 연산 개수
A = [list(map(int, input().split())) for _ in range(N)] 
Q = [tuple(map(int, input().split())) for _ in range(K) ]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = 10000

# 각 행의 합 중 최솟값 출력
def minSum(mat):
    return min([sum(m) for m in mat])


# 주어진 쿼리대로 이동
def move(mat, qry):
    r, c, s = qry
    r, c = r-1, c-1  # 정 가운데 기준점
    newMat = deepcopy(mat)
    # 가운데부터 대각선 오른쪽 위를 시작으로 하/좌/상/우 시계방향으로 이동
    for i in range(1, s+1):  # 대각선 이동 횟수
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):  # 대각선으로 i 번 이동한 경우, 하/좌/상/우는 2배씩 이동
                rrr, ccc = rr + dx[w], cc + dy[w]
                newMat[rrr][ccc] = mat[rr][cc]
                rr, cc = rrr, ccc
    return newMat

# 
def dfs(mat, qry):
    global ans
    if sum(qry) == K:  # 모든 쿼리 체크
        ans = min(ans, minSum(mat))
        return
    for i in range(K):
        if qry[i]:  # 쿼리 처리함
            continue
        # 쿼리 적용해 이동
        newMat = move(mat, Q[i])
        qry[i] = 1  # 체크 마킹
        dfs(newMat, qry)
        qry[i] = 0


dfs(A, [0 for i in range(K)])  # 쿼리 처리했으면 1, 안했으면 0
print(ans)