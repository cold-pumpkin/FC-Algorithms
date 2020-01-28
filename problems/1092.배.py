# 1092. 배

# 매 분마다 모든 크레인에 대해 옮길 수 있는 박스를 선택하여 옮김
# 박스 무게 내림차순 정렬 후 무거운 것 부터 옮김
# 시간복잡도 O(NM)

n = int(input())
limit = list(map(int, input().split()))
limit.sort(reverse=True)


boxes = int(input())
weights = list(map(int, input().split()))
weights.sort(reverse=True)

count = 0

print(limit)
print(weights)