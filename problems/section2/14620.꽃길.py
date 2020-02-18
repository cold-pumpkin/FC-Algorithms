# 14620. 꽃길

N = int(input())
G = [ list( map(int,input().split()) ) for _ in range(N) ]

# 상하좌우
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

ans = 10000

# 꽃잎 위치의 화단 총 가격 체크
def check(seeds):
    cost = 0
    leaves = [] # 세 꽆들의 꽃잎 위치
    for seed in seeds:
        # 각 씨앗의 좌표
        x = seed // N  # 행
        y = seed % N   # 열
        if not(0 < x < N-1 and 0 < y < N-1):
            return 10000
        for d in range(5):
            leaves.append((x+dx[d], y+dy[d]))
            cost += G[x+dx[d]][y+dy[d]]
    # 3개의 꽃 = 15개의 꽃잎일 경우 대힌 비용 리턴
    if len(set(leaves)) == 15:
        return cost
    return 10000


# 씨앗을 심을 수 있는 3개 위치를 전수조사, 비용 최소인 경우 찾기
for i in range(N * N):  # i, j, k는 각 칸의 숫자를 의미
    for j in range(i+1 * N):
        for k in range(j+1 * N):
            # 최소 비용 출력
            ans = min(ans, check([i, j, k]))

print(ans)