# 16165. 걸그룹 마스터 준석이

# N : 입력받을 걸그룹 수
# M : 문제 수

N, M = map(int, input().split())

# 걸그룹 입력
groups = {}
for _ in range(N):
    # {팀이름 : [멤버1, 멤버1, ...]}
    team = input()
    groups[team] = []
    for i in range(int(input())):
        groups[team].append(input())  # {멤버: 팀이름} 도 추가하면 출력에서 쉽게 구현 가능
        
# 문제
for _ in range(M):
    question = input()
    if '1' == input():
        # 멤버 이름 -> 팀 이름 출력
        for k, v in groups.items():
            if question in v:
                print(k)
                break
    else:
        # 팀 이름 -> 멤버 이름 출력
        print('\n'.join(sorted(groups[question])))