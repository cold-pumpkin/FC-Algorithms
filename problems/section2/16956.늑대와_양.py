# 16969. 늑대와 양

# 1. 입력값 받아 목장, 이동경로 설정
R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  # 상/하/좌/우

# 2. 늑대가 양이 있는 칸으로 이동할 수 있는지 체크
#    : 바로 상하좌우에 양이 있는 경우에만 이동이 가능 
check = False
for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                # 범위 정합성 체크
                if 0 <= x < R and 0 <= y < C:
                    if M[x][y] == 'S':
                        check = True

# 3. 이동할 수 있다면 모든 칸을 늑대로 채우기
if check:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] == '.':
                M[i][j] = 'D'
    for m in M:
        print(''.join(m))