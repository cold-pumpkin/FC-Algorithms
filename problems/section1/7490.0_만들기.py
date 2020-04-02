# 7490. 0 만들기
import copy

# 연산자 배열 채우기
def recursive(arr, n):
    if len(arr) == n:
        operators_list.append(copy.deepcopy(arr))
        return

    # 1) 공백
    arr.append(' ')
    recursive(arr, n)
    arr.pop()  # 연산자 조합 길이가 n인 경우 하나 빼기

    # 2) 덧셈
    arr.append('+')
    recursive(arr, n)
    arr.pop()

    # 3) 뺄셈
    arr.append('-')
    recursive(arr, n)
    arr.pop()


t = int(input())
for _ in range(t):
    n = int(input())
    nums = [i for i in range(1, n+1)]

    operators_list = []
    recursive([], n-1)  # 연산자 채우기 (연산자 조합은 n-1개로 구성됨)

    for operators in operators_list:
        expr = ""
        # 식 만들기
        for i in range(n-1):
            expr += str(nums[i]) + operators[i]
        expr += str(nums[-1])
        if eval(expr.replace(" ", "")) == 0:
            print(expr)
    print()
    
