# 1325. 효율적인 해킹
# BFS / DFS
from collections import deque

def bfs(v):  # (노드번호)
    q = deque([v])
    visited = [False] * (N+1)
    # 방문
    visited[v] = True
    count = 1
    # 인접노드들에 대해서 재귀호출 
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    return count


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
max_value = -1
answer = []

# 신뢰관계 입력
for _ in range(M):
    a, b = map(int, input().split())
    adj[b].append(a)

# 각 노드에 대해서 bfs 수행 -> 가장 많이 연결할 수 있는 노드 찾기
for i in range(1, N+1):
    # bfs 수행횟수
    c = bfs(i)
    if c > max_value:
        answer = [i]
        max_value = c
    elif c == max_value:
        answer.append(i)
        max_value = c

for ans in answer:
    print(ans, end = ' ')