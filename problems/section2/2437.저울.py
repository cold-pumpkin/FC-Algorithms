# 2437. 저울

N = int(input())
A = sorted(list(map(int, input().split())))

# 어떤 값 S 까지 만들 수 있다고 할 때, S+1이 있으면 
# 지금까지 방법대로 계속 더해나갈 수 있음
# ex) 1 2 3 7 ... => 6 만들 수 있음. 7이 존재. 8부터 계속 만들 수 있음
# ex) 1 2 3 8 ... => 6 만들 수 있지만, 7은 만들 수 없음

ans = 0  # 측정할 수 있는 최소값
for i in A:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans+1)  # 측정할 수 없는 최소값