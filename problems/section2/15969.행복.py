# 15969. 행복

# 정렬

n, grades = input(), list(map(int, input().split(' ')))
#grades = list(map(int, input().split(' ')))
print(max(grades) - min(grades))