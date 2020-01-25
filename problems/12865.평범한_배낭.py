# 12865. 평범한 배낭 (knapsack problem)

# 물품의 수 N, 배낭에 담을 수 있는 무게가 K 일 때, O(NK)로 해결
# D[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치
# 각 물품번호 i에 따라 최대 가치를 저장하고 있는 테이블인 D[i][j]를 갱신

n, k = map(int, input().split())  # 물품 개수, 최대 가능 무게
dp = [[0] * (k+1) for _ in range(n+1)]  # dp[물건번호][무게] = 최대 가치

for i in range(1, n+1):
    weight, value = map(int, input().split())
    # 무게, 가치 계산 채우기
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]  # 이전 물품까지의 가치 가져오기
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)  # 이전 물품의 이전 무게의 가치 + 현재 물품의 가치

print(dp[n][k])