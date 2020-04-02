# 1697. 숨바꼭질

# 특정 위치까지 이동하는 최단 시간 
# 이동 시간이 모두 1초로 동일하므로, BFS 이용하여 해결 가능
# 시작 정점에서부터 갈 수 있는 정점들을 그래프 형태로 구현, 탐색

from collections import deque
MAX = 100001
n, k = map(int, input().split())  # 시작 정점, 목표 정점
array = [0] * MAX  # 해당 정점까지 거쳐온 간선의 길이 

def bfs():
    q = deque([n])
    while q:
        cur_pos = q.popleft()
        # 목표 정점에 도착했으면 거리 리턴
        if cur_pos == k:
            return array[cur_pos]
        # 탐색 가능한 다음 포지션을 방문하지 않은 경우 덱에 삽입 & 거리 증가
        for next_pos in (cur_pos-1, cur_pos+1, cur_pos*2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[cur_pos] + 1
                q.append(next_pos)

print(bfs())