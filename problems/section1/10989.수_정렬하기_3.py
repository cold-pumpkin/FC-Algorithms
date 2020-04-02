# 10989. 수 정렬하기 3

# 계수정렬(Counting Sort) 알고리즘
# - 배열의 인덱스에 해당하는 빈도 수를 넣어서 최종적으로 인덱스를 차례로 빈도 수만큼 출력
# - 주어진 데이터의 범위가 정해져있을 때 사용
import sys

count = [0] * 10001 # 데이터 : 10,000보다 작거나 같은 자연수

n = int(input())
for _ in range(n):
    i = int(sys.stdin.readline())
    count[i] += 1

for i in range(10001):
    if count[i] != 0:
        for c in range(count[i]):
            print(i)


