# 1543. 문서 검색

doc = input()
word = input()

index = 0
result = 0

while index + len(word) <= len(doc):
    if doc[index:index+len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)