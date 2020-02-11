# 16769. Mixing Milk

N = 3
capacity = [0] * N
milk = [0] * N
for i in range(N):
    capacity[i], milk[i] = map(int, input().split())

M = 100
for i in range(M):
    cur = i % N
    nxt = (cur + 1) % N
    pour = min(milk[cur], capacity[nxt]-milk[nxt])
    milk[cur] -= pour
    milk[nxt] += pour

for m in milk:
    print(m)