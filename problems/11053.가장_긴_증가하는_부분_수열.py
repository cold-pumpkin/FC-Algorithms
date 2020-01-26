# 11053. 가장 긴 증가하는 부분 수열 (LIS)

# 수열 크기가 N일 때, 동적 프로그램으로 O(n^2)로 해결 가능
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n  # 초기값을 1로 셋팅

for i in range(1, n):
    # i와 그 앞의 수들과 비교, 증가하는 부분 수열이면 1 증가
    # dp[i]에는 그 중에서도 최대값을 유지
    for j in range(0, i): 
        if array[j] < array[i]:  # 증가하는 부분 수열 확인
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))