# 2751. 수 정렬하기 2
#  - 고급 정렬 알고리즘

# merge sort : nlogn

def merge(left, right):
    merged_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    
    if i < len(left):
        while i < len(left):
            merged_list.append(left[i])
            i += 1
    
    if j < len(right):
        while j < len(right):
            merged_list.append(right[j])
            j += 1            
    return merged_list

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    return merge(merge_sort(left), merge_sort(right))


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)


# array = sorted(array)