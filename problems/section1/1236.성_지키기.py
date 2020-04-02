# 1236. 성 지키기

n, m = map(int, input().split())
castle = []

for _ in range(n):
    castle.append(input())

row = [0] * n
col = [0] * m
for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X': # 행/열에 X가 있으면 1, 없으면 0
            row[i] = 1
            col[j] = 1 


# 행, 열로 탐색해서 채워야 할 것이 더 큰 쪽
row_cnt = 0
for i in range(n):
    if row[i] == 0:
        row_cnt += 1

col_cnt = 0
for j in range(m):
    if col[j] == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))
