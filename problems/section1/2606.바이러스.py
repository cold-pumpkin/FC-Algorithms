# 2606. 바이러스
# BFS / DFS

V = int(input())
E = int(input())
adj = [[] for _ in range(V+1)]
visited = [False] * (V+1)
count = 0

# 간선 정보 입력
for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# DFS 탐색
def dfs(cur):
    global count
    # 방문
    count += 1
    visited[cur] = True
    # 아직 방문하지 않은 이웃 노드들에 대해 재귀호출
    for next_v in adj[cur]:
        if not visited[next_v]:
            dfs(next_v)

dfs(1)
print(count-1)  # 시작정점을 방문한 경우 카운트 빼기


