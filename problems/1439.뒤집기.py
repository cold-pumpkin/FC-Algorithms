# 1439. 뒤집기

# 모두 0으로 만드는 경우 / 1로 만드는 경우 비교
# 주어진 수를 앞에서부터 2개 원소씩 비교, 숫자가 바뀌면 

data = input()
count0 = 0  # 전부 0로 바꾸기
count1 = 0  # 전부 1로 바꾸기

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    # 숫자가 바뀌는 시점까지 진행
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))