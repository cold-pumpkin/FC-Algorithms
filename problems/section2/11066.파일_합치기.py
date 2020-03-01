# 11066. 파일 합치기

def process():
    N = int(input())  # 챕터 수
    A = [0] + list(map(int, input().split()))  # 모든 챕터의 페이지 수
    
    # 누적합 활용
    # DP[i][j] : i에서 j까지 합치는데 필요한 최소 비용
    # DP[i][j] = DP[i][k] + DP[k+1][j] + sum(A[i] ~ A[j])
    #          => 이때, sum(A[i] ~ A[j])은 고정값이므로, 
    #             DP[i][k] + DP[k+1][j]가 최소가 되는 k값 찾는 것이 관건

    # S[i] : 1번 부터 i번 까지의 누적 페이지 합
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]
    DP = [[0] * (N+1) for _ in range(N+1)]

    # 부분합 구하기

    for i in range(2, N+1):  
        # i : 합칠 부분파일의 길이 (3개를 합칠 경우 1개+2개 or 2개+1개 합치는 경우 존재하므로, 2개씩 합칠 때 배용 구해놔야 함)
        for j in range(1, N+2-i):  
            # j : 시작점 (j에서 i만큼 떨어진 지점 까지)
            # j부터 길이가 i인 파일까지 합쳤을 때 최소 비용 
            #   = min(j에서 k만큼 떨어진 지점의 파일들을 합칠 때 비용 합 + 나머지 파일들 합칠 때 비용 합) .. 중 최소 비용
            #    + 원본 배열에서의 합
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])
    print(DP)
    print(DP[1][N])

T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    process()