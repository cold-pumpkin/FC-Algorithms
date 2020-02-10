# 9037. The candy war (다른 풀이)

def check(N, candy):
    # 짝수 만들기
    for i in range(N):
        if candy[i] % 2 != 0:
            candy[i] += 1
    return len(set(candy)) == 1


def giveCandy(N, candy):
    temp_list = [0 for i in range(N)]
    # 짝수 만들고 오른쪽으로 패스
    for i in range(N):
        if candy[i] % 2 != 0:
            candy[i] += 1
        
        candy[i] //= 2  # 반만 남기기
        temp_list[(i+1) % N] = candy[i]  # 오른쪽에 더해줄 수

    for i in range(N):
        candy[i] += temp_list[i]

    return candy


def playCandyWar():
    N, candy = int(input()), list(map(int, input().split()))
    cycle = 0
    # 모두가 같은 수의 캔디를 갖게 될 때까지 반복
    while not check(N, candy):
        cycle += 1
        canday = giveCandy(N, candy)
    print(cycle)



# 테스트 케이스 수 만큼 반복
for _ in range(int(input())):
    playCandyWar()