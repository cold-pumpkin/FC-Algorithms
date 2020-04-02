n = int(input())

coordinate = []
for _ in range(n):
    x, y = map(int, input().split(' '))
    coordinate.append((x, y))

coordinate = sorted(coordinate) # 내부적으로 ㅌ

for c in coordinate:
    print(c[0], c[1])

    