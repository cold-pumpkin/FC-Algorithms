# 5585. 거스름돈

# 가장 기초적인 탐욕 알고리즘 문제 유형
# 단순히 가장 큰 화폐 단위로 잔돈 거슬러주면 최적의 해 구할 수 있음

change = 1000 - int(input())
count = 0

for i in (500, 100, 50, 10, 5, 1):
    count += change // i
    change %= i

print(count)