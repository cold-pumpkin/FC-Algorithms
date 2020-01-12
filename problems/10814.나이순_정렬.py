# 10814. 나이순 정렬

n = int(input())
names = [[] for _ in range(201)]

for _ in range(n):
    i, name  = input().split()
    names[int(i)].append(name)

for a in range(1, len(names)):
    if names[a]:
        for name in names[a]:
            print(a, name)