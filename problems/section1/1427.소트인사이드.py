# 1427. 소트인사이드

nums = []
ipt = input()

for i in range(len(ipt)):
    nums.append(ipt[i])

nums.sort(reverse=True)
print(''.join(nums))