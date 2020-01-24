# 2250. 트리의 높이와 너비

# 노드 구현
class Node:
    def __init__(self, data, left, right):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right

n = int(input())  # 노드 개수
min_level = [n]  # 레벨별 가장 왼쪽 노드 위치
max_level = [0]  # 레벨별 가장 오른쪽 노드 위치

# 중위 순회 구현 (전체 트리의 맨 왼쪽부터)
depth = 1
pos = 1
def inorder_traversal(node, level):
    global depth, pos
    depth = max(depth, level)
    
    if node.left != -1:
        inorder_traversal(tree[node.left], level+1)
    min_level[level] = min(min_level[level], pos)
    max_level[level] = max(max_level[level], pos)
    pos += 1
    if node.right != -1:
        inorder_traversal(tree[node.right], level+1)


tree = {}         # {data : Node}
# 트리, 노드 최대/최소 위치 초기화
for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)
    min_level.append(n)
    max_level.append(0)

# 입력받은 값으로 트리 셋팅
for _ in range(n):
    data, left, right = map(int, input().split())
    tree[data].left = left
    tree[data].right = right
    # 왼쪽 자식이 존재하면 현재 노드를 그 왼쪽 자식의 부모 노드로 셋팅 
    if left != -1:
        tree[left].parent = data 
    # 오른쪽 자식이 존재하면 현재 노드를 그 오른쪽 자식의 부모 노드로 셋팅 
    if right != -1:
        tree[right].parent = data

# 루트 노드 찾기
root = -1
for i in range(1, n+1):
    if tree[i].parent == -1:
        root = i

inorder_traversal(tree[root], 1)

# 너비가 가장 가장 넓은 레벨과 너비 출력
result_level = 1
result_width = max_level[1] - min_level[1] + 1
for i in range(2, depth+1):
    cur_width = max_level[i] - min_level[i] + 1
    if result_width < cur_width:
        result_level = i
        result_width = cur_width

print(result_level, result_width)