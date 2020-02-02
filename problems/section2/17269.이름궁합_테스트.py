import copy
 
n, m = list(map(int, input().split()))
a, b = input().split()

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1,
         3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 
         1, 1, 1, 2, 2, 1]

# 문자열 합치기
ab = ''
min_len = min(n, m)
for i in range(min_len):
    ab += a[i] + b[i]
ab += a[min_len:] + b[min_len:]

# 알파벳 -> 숫자 리스트로 변환
array = [alpha[ord(s)- ord('A')] for s in ab]  # ord() : 아스키 코드 값 반환

# 뒤 요소를 앞 요소에 더해 줌
for i in range(n+m-2):  # 전체 반복횟수 : 요소가 두개 남을 때까지
    for j in range(n+m-1-i):  # 다음 요소를 앞 요소에 더해줌 : 요소가 i개씩 줄어듦
        array[j] += array[j+1]

print("{}%".format(array[0] % 10 * 10 + array[1] % 10))