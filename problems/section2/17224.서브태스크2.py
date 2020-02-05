# 17224. APC는 왜 서브태스크 대회가 되었을까? (다른 풀이)

# N : 문제 개수
# L : 역량 (L 이하의 난이도만 풀 수 있음)
# K : 풀 수 있는 문제 최대 개수 
# sub1 : 쉬운 버전 난이도, sub2 : 어려운 버전 난이도

N, L, K = map(int, input().split())

easy, hard = 0, 0
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    # K 상관없이 풀 수 있는 어려운/쉬운 문제 수 구하기
    # 단, 어려운 문제 수를 우선 입력
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# 어려운 문제부터 점수 계산 (K개 까지 해결 가능)
score = min(hard, K) * 140

# 풀 수 있는 어려운 문제 수가 K보다 작았다면
# 쉬운 문제 풀기
if hard < K:
    score += min(K-hard, easy) * 100

print(score)