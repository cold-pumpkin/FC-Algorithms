# 16676. 근우의 다이어리 꾸미기

# 0   ~ 10   (< 11)   : 스티커팩 1개
# 11  ~ 110  (< 111)  : 스티커팩 2개
# 111 ~ 1110 (< 1111) : 스티커팩 3개
# ...

N = input()
S = '1' * len(N)

if len(N) == 1:
    print(1)
elif int(N) >= int(S):
    print(len(N))
else:
    print(len(N)-1)