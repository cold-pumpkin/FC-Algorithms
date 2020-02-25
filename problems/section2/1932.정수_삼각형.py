# 1932. 정수 삼각형

# 모든 경로를 탐색하면 2의 제곱으로 경우의 수가 급격히 증가함
# DP 점화식을 세워서 접근

N = int(input())  # 삼각형 크기
T  = [[0]*(N+1) for _ in range(N+1)]  # 삼각형 : 인덱스 오류를 방지하기 위해 0 한 행,열 더 넣어줌

# DP[i][j] : (i,j)에 도착했을 때의 최댓값
# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + T[i][j]
DP = [[0]*(N+1) for _ in range(N+1)]

# 삼각형 채우기
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, i+1):
        T[i][j] = row[j-1]

# 점화식 구현
for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + T[i][j]

print(max(DP[-1]))