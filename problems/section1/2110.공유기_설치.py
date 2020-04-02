# 2110. 공유기 설치

# N은 최대 200,000 X는 최대 1,000,000,000
# --> 이진탐색을 이용해 O(NlogX)로 해결
# 가장 인접한 두 공유기 사이의 최대 gap을 이진탐색으로 찾기

n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

# 초기 최소 gap : array 1번째, 2번째 집 gap
# 초기 최대 gap : array 1번째, 마지막 집 gap
# -> 정답 후보 gap을 (최소+최대)/2 로 설정하고 공유기를 설치해 봄
#    설정한 gap 이상이 되는 집에 설치할 수 있는지 확인
#    - 불가능하다면 최대 gap을 줄여서 다시 확인
#    - 가능하다면 최대 gap을 하나 늘려서 다시 확인

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0  # 가능한 최대 gap

# 이진 탐색
while start <= end:
    mid = (start + end) // 2  # 정답 후보 gap
    # mid 이상의 gap으로 공유기 설치 가능한지 확인
    criteria = array[0]
    count = 1  # 공유기 수
    # 가장 왼쪽 집부터 공유기 설치
    for i in range(1, len(array)):
        if array[i] >= criteria + mid:
            criteria = array[i]
            count += 1

    # c개 이상의 공유기 설치 가능하면 결과 저장, gap 증가
    if count >= c:
        start = mid + 1  # 더 좁은 범위에서 탐색
        result = mid
    else:
        end = mid - 1

print(result)