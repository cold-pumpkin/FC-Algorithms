# 17224. APC는 왜 서브태스크 대회가 되었을까?

# N : 문제 개수
# L : 역량 (L 이하의 난이도만 풀 수 있음)
# K : 풀 수 있는 문제 최대 개수 
# sub1 : 쉬운 버전 난이도, sub2 : 어려운 버전 난이도

N, L, K = map(int, input().split())

score = 0
solved = 0
easy, hard = [], []
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    easy.append(sub1)
    hard.append(sub2)

easy.sort()
hard.sort()

for i in range(N):
    if hard[i] <= L:
        if solved < K:    
            score += 140
            solved += 1
    else:
        if easy[i] <= L:
            if solved < K:    
                score += 100
                solved += 1

print(score)
