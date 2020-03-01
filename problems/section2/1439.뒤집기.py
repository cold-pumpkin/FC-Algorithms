# 1439. 뒤집기

S, cnt = input(), 0

# 바뀌는 지점 카운트
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        cnt += 1

print((cnt+1)//2)