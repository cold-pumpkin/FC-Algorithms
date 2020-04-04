# 9251. LCS (Longest Common Subsequence)
# 동적 프로그래밍

# D[i][j] : X[0..i]와 Y[0..1] 의 공통 부분 수열의 최대 길이
A, B = input(), input()

# 공집합 포함해 테이블 생성
dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1  # 문자열이 같은 경우 대각선 왼쪽 위에서 1 더해줌
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 위, 왼쪽값 중 큰 값 대입

print(dp[len(A)][len(B)])