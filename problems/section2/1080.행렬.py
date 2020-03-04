# 1080. 행렬

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]


# 3*3 행렬 단위로 뒤집기
def flip(x, y, A):
    for i in range(3):
        for j in range(3):
            A[x+i][y+j] ^= 1  # XOR 연산으로 0이면 1, 1이면 0으로 만들기


# 첫번째 점이 뒤집히는지 안다면, 다음 점이 뒤집혀야하는지 아닌지 알 수 있음
ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:  # A와 B의 기준 요소의 값이 다르면 뒤집기
            flip(i, j, A)
            ans += 1

print(ans if A == B else -1)