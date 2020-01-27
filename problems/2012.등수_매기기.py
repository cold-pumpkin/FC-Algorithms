# 2012. 등수 매기기

# 실제와 예상 등수 차이를 최소화 하기 위해서는 예상 등수를 오름차순 정렬

n = int(input())
expectation = [int(input()) for _ in range(n)]
expectation.sort()

result = 0
for i in range(1, n+1):
    result += abs(i - expectation[i-1])

print(result)
