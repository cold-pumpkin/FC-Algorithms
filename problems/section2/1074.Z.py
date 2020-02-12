# 1074. Z

N, r, c = map(int, input().split())

def Z(size, row, col):
    # base condition
    if size == 1:
        return 0

    half = size // 2
    # 4등분한 사각형
    for i in range(2):
        for j in range(2):
            # 순서대로 0/1/2/3 번째 칸을 의미
            if row < half * (i + 1) and col < half * (j + 1):
                # 다음 칸으로 가는 규칙
                return (i*2+j) * (half ** 2) + Z(half, row - half * i, col-half*j)

'''
(0 0) (0 1) (1 0) (1 1) 
 0     1     2     3
=> i*2+j
'''

print(Z(2 ** N, r, c))