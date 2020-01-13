# 1074. Z

answer = 0

# Z 모양으로 이동
def move(n, r, c):
    global answer

    # Base condition - 2*2 행렬인 경우 Z 이동하며 확인
    if n == 2:
        if r == R and c == C:
            print(answer)
            return
        answer += 1

        if r == R and c+1 == C:
            print(answer)
            return
        answer += 1

        if r+1 == R and c == C:
            print(answer)
            return
        answer += 1

        if r+1 == R and c+1 == C:
            print(answer)
            return
        answer += 1
        return
    
    # 4조각으로 나눠서 재귀호출
    move(n/2, r, c)
    move(n/2, r, c+n/2)
    move(n/2, r+n/2, c)
    move(n/2, r+n/2, c+n/2)

# 2^N * 2^N 배열, (R, C) 번째 칸
N, R, C = map(int, input().split(' '))

move(2 ** N, 0, 0)