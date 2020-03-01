# 1915. 가장 큰 정사각형

N, M = map(int, input().split())

# DP[i][j] = (i,j) 까지 왔을 때 가장 큰 정사각형의 한 변의 길이

# S          DP
# 0 1 1      0 1 1
# 1 1 1  =>  1 1 2  =>  ? = min(2, 2, 1) + 1 = 2
# 1 1 1      1 2 ?
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
DP = [[0]* (M+1) for _ in range(N+1)]  # 행, 열 1개씩 0으로 더 추가

S = [[0] * (M+1)]
S += [[0] + list(map(int, input())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if S[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1

print(max(max(d) for d in DP) ** 2)