# 11055. 가장 큰 증가 부분 수열

import copy

N = int(input())
A = list(map(int, input().split()))

# DP[i] : i까지 증가 부분 수열의 합의 최댓값
DP = copy.deepcopy(A)

# 현재 위치 이전 요소 중 작은 값 더해주면서 갱신
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(A[i]+DP[j], DP[i])

print(max(DP))