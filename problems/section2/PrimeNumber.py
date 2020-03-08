# 소수 찾기와 소인수 분해

# 소수 확인 기본 : O(sqrt(N))
def prime_check(N):
    for i in range(2, N):
        if N % i == 0:
            return False
        if i * i > N:
            break
    return True


# 소인수분해 기본 (소인수 리스트 찾기) : O(sqrt(N))
# 소인수 : 주어진 자연수를 나누어 떨어뜨리는 약수 중에서 소수인 약수
def prime_factorization(N):
    p, fac = 2, []  # 나눌 수 ,소인수 저장할 리스트
    while p ** 2 <= N:
        if N % p == 0:
            N //= p  # N을 줄여줌
            fac.append(p)
        else:
            p += 1
    if N > 1:
        fac.append(N)
    return fac

print('소인수 출력 : ', prime_factorization(12345))

# 에라토스테네스의 체를 활용한 소수 리스트 구하기 (효율적)
# : 전체 수 리스트 중 1 지우고, 2 배수들 지우고, 3 배수들 지우고, ...
# : 소수 리스트를 미리 만들어두는 방식
def era_prime(N):
    A, p = [0 for _ in range(N+1)], []  # [소수 : 0, 합성수 : 1], [소수들]
    for i in range(2, N):
        if A[i] == 0:  # 소수라고 판단된 상태인 경우
            p.append(i)
        # 제곱수부터 시작해서 배수 지우기
        for j in range(i**2, N, i):
            A[j] = 1  # 합성수로 판단
    return p

print('에라토스테네스의 체를 이용한 소수 출력 : ', era_prime(100))


# 소수 리스트가 있는 경우 소인수분해
# 소수 리스트의 크기는 sqrt(N)보다 커야함
def prime_factorization2(N, p):  # (N의 소인수 찾기, N 이하 소수 리스트)
    fac = []  # 소인수 리스트
    for i in p:
        if N == 1 or i*i > N :
            break
        while N % i == 0:
            N //= i
        fac.append(i)
    return fac

print('소수 리스트를 이용한 소인수 출력 : ', prime_factorization2(100, era_prime(100)))


# 에라토스체네스의 체 활용

# 1) 소인수 개수 구하기
def era_fator_count(N):
    A = [0 for _ in range(N+1)]  # 소인수의 개수를 저장할 리스트
    for i in range(2, N+1):
        if A[i] == 0:  # 소수이면
            for j in range(i, N+1, i): # j
                A[j] += 1  # i의 배수이면 1증가 (개수 갱신)
    #print(f'{N}의 소인수 개수 : ', A)
    return A[N]

print('소인수 개수 : ', era_fator_count(12345))

# 2) 소인수들의 합
def era_factor_sum(N):
    A = [0 for _ in range(N+1)]  # 소인수들의 합을 저장할 리스트
    for i in range(2, N+1):
        if A[i] == 0:  # 소수이면
            for j in range(i, N+1, i):
                A[j] += i   # i의 배수이면 i만큼 증가 (합 갱신)
    return A[N]

print('소인수들의 합 : ', era_factor_sum(60))

# 3) 소인수 분해하기
def era_factorization(N):
    A = [0 for _ in range(N+1)]  # N까지의 소인수들을 저장할 리트스
    for i in range(2, N):
        if A[i] == 0:
            for j in range(i, N, i):
                A[j] = i
    return A

# 소인수 분해
A = era_factorization(100)
N = 84

# N이 몇개의 어떤 소인수들로 이루어져있는지 확인
print(f'{N} 소인수 분해')
while A[N] != 0:
    print(A[N])  # N을 나눌 소인수
    N //= A[N]



# 빠른 거듭제곱과 모듈러 (파이썬에는 pow(a, b, mod) 사용하면 되므로 해당되지 않음)
# ex) a^11 = a^1 * a^2 * a^8

