# 1092. 배

# 매 분마다 모든 크레인에 대해 옮길 수 있는 박스를 선택하여 옮김
# 박스 무게 내림차순 정렬 후 무거운 것 부터 옮김
# 시간복잡도 O(NM)
import sys

n = int(input())
limit = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

# 모든 박스 옮길 수 없는 경우
if max(limit) < max(boxes):
    print(-1)
    sys.exit()

# 무거운 것 부터 옮기기 위해 내림차순 정렬
limit.sort(reverse=True)
boxes.sort(reverse=True)

checked = [False] * m  # 박스를 옮겼는지 체크
position = [0] * n     # 각 크레인이 옮겨야 하는 박스 번호
count = 0   # 현재까지 몇개 옮겼는지 체크
result = 0  # 걸리는 시간

while True:  # 매 분마다
    if count == m:
        break
    for i in range(n):  # limit
        # 각 크레인에 대해 박스 무게를 탐색하며 옮길 수 있는지 체크
        while position[i] < m:
            if not checked[position[i]] and limit[i] >= boxes[position[i]]:
                checked[position[i]] = True
                position[i] += 1
                count += 1
                break
            position[i] += 1
    result += 1

print(result)