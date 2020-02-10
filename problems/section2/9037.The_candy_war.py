# 9037. The candy war
import copy

T = int(input())

for _ in range(T):
    N = int(input())
    candy = list(map(int, input().split()))
    # 짝수 만들기
    for i in range(N):
        if candy[i] % 2 != 0:
            candy[i] += 1
    
    # 싸이클 시작
    cycle = 0
    while True:
        if N == 1:
            print(0)
            break
        if min(candy) == max(candy):
            print(cycle)
            break

        # 오른쪽 사람에게 반씩 넘겨주기
        for i in range(N):
            candy[i] //= 2

        half = copy.deepcopy(candy)
        for i in range(1, N):
            candy[i] += half[i-1]
        candy[0] += half[-1]
        # 짝수 만들기
        for i in range(N):
            if candy[i] % 2 != 0:
                candy[i] += 1
        
        cycle += 1