# 10814. 나이순 정렬 (강사 풀이)

n = int(input())
names = []

for _ in range(n):
    i, name  = input().split()
    # (나이, 이름) 튜플 형식으로 저장
    names.append((int(i), name))

names = sorted(names, key=lambda x: x[0]) # 튜플의 앞 원소(나이)에 대해 정렬

for name in names:
    print(name[0], name[1])
