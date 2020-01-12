''' 
# 4195 : 친구 네트워크

# Union-find 
'''
# 부모 찾기 
def find(x):
    if x == parent[x]:
        return x 
    else:
        # 재귀적으로 최상위 부모 찾기
        p = find(parent[x])
        parent[x] = p
        return parent[x]  # 부모값 반환

# 합집합
def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x  # 최상위 부모끼리 연결
        number[x] += number[y]  # 다른 네트워크간 개수 합치기

n = int(input())

for _ in range(n):
    parent = {}  # {자식 : 부모}
    number = {}
    for _ in range(int(input())):
        x, y = input().split(' ')
        if x not in parent:
            parent[x] = x  # 처음 값은 자기 자신으로 초기화
            number[x] = 1
        if y not in parent:
            parent[y] = y 
            number[y] = 1
        
        union(x, y)

        print(number[find(x)])
