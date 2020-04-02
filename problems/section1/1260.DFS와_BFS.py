# 1260. DFS와 BFS

# 모든 노드와 간선을 차례대로 조회하여 O(N+M)의 시간 복잡도로 문제 해결
# 큐 구현을 위해 collection 라이브러리의 deque 사용
# 외울 정도로 연습!

from collections import deque

n, m, v = map(int, input().split())  # 정점 개수, 간선 개수, 시작 정점
adj = [[] for _ in range(n+1)]  # 연결리스트로 이웃하는 정점 저장

# 이웃 정점 저장
for _ in range(m):
    x, y = map(int, input().split())
    # adj 안의 x번째 리스트에 x와 연결된 정점들 저장
    # adj 안의 y번째 리스트에 y와 연결된 정점들 저장
    adj[x].append(y)  
    adj[y].append(x)

# 이웃하는 정점 중 번호가 작은 것 부터 방문하므로, 내부를 정렬
for a in adj:
    a.sort()

# DFS
def dfs(v):
    # 방문
    print(v, end=' ')  
    visited[v] = True
    # 시작 정점 방문 후 그 정점에 이웃한 다음 정점 중 
    # 가장 작은 번호의 정점 방문
    for e in adj[v]:
        if not visited[e]:  
            dfs(e)


# BFS
def bfs(v):
    q = deque([v])
    # 방문할 정점 deque에 넣으면서 방문
    while q:
        v = q.popleft()
        if not visited[v]:
            # 방문
            print(v, end=' ')
            visited[v] = True
            # 방문한 정점과 이어진 모든 정점부터 deque에 넣기
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)