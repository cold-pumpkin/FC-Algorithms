# 2167. 2차원 배열의 합

# 시간복잡도를 줄이기 위해 누적합 활용
# * 1차원 배열
# DP[i] = 0부터 i까지의 누적된 합
# i부터 j까지 의 합 = DP[i] - DP[j-1]

# * 2차원 배열
# DP[i][j] = (1,1)부터 (i,j)까지 부분합
#          = 위에서 가져온 누적합 + 왼쪽에서 가져온 누적합 - 대각선에서 가져온 누적합 + 원래 배열 자리

N, M = map(int, input().split())  # 행/열
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (M+1) for _ in range(N+1)]  # i, j, x, y가 1부터 시작하므로

# 2차원 배열의 누적합(DP) 셋팅
for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]  # A배열 인덱스 주의

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    # (x,y)까지 부분합 - (i-1,y)까지 부분합 - (x,j-1)까지 부분합 + (i-1,j-1)까지 부분합(중복제거 되었던 부분)
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])