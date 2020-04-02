# 1668. 트로피 진열

n = int(input())
height = [ int(input()) for _ in range(n) ]

# 오름차순으로 나열된 트로피 개수 카운트
def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result

print(ascending(height))
height.reverse()
print(ascending(height))
