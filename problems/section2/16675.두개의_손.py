# 16675. 두 개의 손

# 가위, 바위, 보를 각각 0, 1, 2로 변환
ML, MR, TL, TR = ('SRP'.index(i) for i in input().split())

# 확실한 경우 - TK 승리
if ML == MR and (ML+1) % 3 in [TL, TR]:
    print("TK")
# 확실한 경우 - MS 승리
elif TL == TR and (TL+1) % 3 in [MR, ML]:
    print("MS")
else:
    print("?")