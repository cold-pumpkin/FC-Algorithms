# GCD (Greatest Common Divisor)

# 방법 1 : 단순한 반복문 사용. 두 수 중 작은 수부터 시작해 1씩 뺀 수를 나누어 확인. (복잡도 O(n))
def gcd_naive(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# 방법 2-1 : 유클리드 호제법 이용한 방법 (재귀)
# G(a, b) = G(b, a%b)
def gcd1(a, b):
    if a % b == 0:
        return b
    return gcd1(b, a%b)
    #return gcd(b, a%b) if a % b != 0 else b

# 방법 2-2 : 유클리드 호제법 이용한 방법 (반복문)
def gcd2(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b

# 방법 3 : math 라이브러리의 gcd 활용
import math
math.gcd(1, 2)

# 연산 속도는 아래로 갈 수록 더 빠름
print(gcd_naive(10, 24))
print(gcd1(10, 24))
print(gcd2(10, 24))
print(math.gcd(10, 24))


# LCM (Least Common Multiple)

# LCM(a, b) = a * b / GCD(a, b)
# int overflow 고려하여 a / GCD(a, b) * b 도 가능

def lcm(a, b):
    return a*b/math.gcd(a,b)