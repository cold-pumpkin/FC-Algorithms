# 1904. 01파일

# 점화식 : D(n+2) = D(n+1) + D(n)

n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])