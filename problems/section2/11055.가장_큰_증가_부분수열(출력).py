# 11055. 가장 큰 증가 부분 수열(출력)

# 합이 가장 큰 증가 부분 수열을 출력 (경로 추적)

import copy

N = int(input())
A = list(map(int, input().split()))

# DP[i] : i까지 증가 부분 수열의 합의 최댓값
DP = copy.deepcopy(A)
R = [i for i in range(N)]  # DP 요소가 갱신될 때, 더한 값의 인덱스를 저장하기 위한 배열

# 현재 위치 이전 요소 중 작은 값 더해주면서 갱신
idx = 0  # DP배열에서 최댓값을 가진 위치 인덱스
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and DP[i] < A[i] + DP[j]:  # DP 배열 갱신 조건
            DP[i] = A[i]+DP[j]
            R[i] = j  # 더한 값의 인덱스 저장
    if DP[idx] < DP[i] :
        idx = i  # DP 배열 최댓값의 인덱스

print(max(DP))

# 더한 경로는 R를 거꾸로 추적
while R[idx] != idx:  # 자기 자신부터 출발하는 인덱스를 만날 때 까지
    print(A[idx], end=' ')  # 더해진 값의 인덱스를 거꾸로 쫓아 감
    idx = R[idx]
print(A[idx])