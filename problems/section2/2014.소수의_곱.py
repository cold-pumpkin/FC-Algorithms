# 2014. 소수의 곱

# 힙(그룹 내에서 가장 큰(작은) 값을 루트에 둠) 활용하기
# (Greedy 문제에서 어려운 편에 속하지만 중요)
import heapq
import copy

K, N = map(int, input().split())
A = list(map(int, input().split()))

# ck : 중복하는 수 표현 x (ex. 2*2*3 == 2*3*2 = 12 이므로 중복값) 
C, ck = copy.deepcopy(A), set()
heapq.heapify(C)  # 리스트 -> 힙으로 변환

ith = 0  # 찾고자 하는 수의 인덱스
while ith < N:
    mn = heapq.heappop(C)  # 루트값(최소값)을 pop 해줌
    if mn in ck:  # 이미 계산한 값이면 스킵
        continue
    
    # 처음 나온 값이면 set에 추가
    ith += 1
    ck.add(mn)

    # [2, 3, 5, 7] 일 때, 2가 pop으로 빠진 다음에는 
    # [3, 5, 7, 2*2, 2*3, 2*5, 2*7] 끼리 비교할 수 있도록 차례로 값을 넣어줌
    # [3, 5, 7]에 3*2(중복), 3*3, 3*5, 3*7을 추가할 때 중복 값은 들어가지 않도록 set을 사용한 것
    for i in A:
        if mn * i < 2**32:  # 시간을 줄이기 위해 문제 조건 활용
            heapq.heappush(C, mn * i)
    
print(mn)