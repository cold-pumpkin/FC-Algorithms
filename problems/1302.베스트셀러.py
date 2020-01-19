# 1302. 베스트셀러 

books = dict()

n = int(input())
for _ in range(n):
    b = input()
    if b not in books:
        books[b] = 1
    else:
        books[b] += 1

#books = {k: v for k, v in sorted(books.items(), key=lambda item: item[1], reverse=True)}

# 가장 큰 value를 가진 키 중 알파벳 순서상 맨 처음 값
max_value = max(books.values())
candidates = []
for book, count in books.items():
    if count == max_value:
        candidates.append(book)

print(sorted(candidates)[0])