# 17389. 보너스 점수

N, S = int(input()), input()

result = 0
bonus = 0
for i, ox in enumerate(S):
    if ox == 'O':
        result += i+1+bonus
        bonus += 1
    else:
        bonus = 0

print(result)