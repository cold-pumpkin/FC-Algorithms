# 12849. 본대 산책

# DP[i] = 각 건물에 도착하는 방법의 수
# 0 : 정보과학관    4 : 한경직기념관
# 1 : 전산관       5 : 진리관
# 2 : 미래관       6 : 학생회관
# 3 : 신양관       7 : 형남공학과
DP = [1, 0, 0, 0, 0, 0, 0, 0]  # 0분에 어떤 지점에 도착할 수 있는 상태

# 1분 동안 다음 건물로 갈 때 마다 DP배열 업데이트
def nxt(state):
    tmp = [0 for _ in range(8)]
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    # 미리 나머지 연산 하는 것이 더 빠름
    for i in range(8):
        tmp[i] %= 1000000007
    return tmp

for i in range(int(input())):
    DP = nxt(DP)

print(DP[0])