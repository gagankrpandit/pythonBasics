# Python program to implement binary search

list = [54, 67, 85, 33, 92, 74]
list.sort()
print(f'Given list is: {list}')

low = 0
upp = len(list)
mid = (low + upp) // 2

num = list.index(int(input('Enter number: ')))

while num != mid:
    mid = (low + upp) // 2
    if num < mid:
        upp = mid
        mid = (low + upp) // 2
    else:
        if num > mid:
            low = mid
            mid = (low + upp) // 2
print(f'found at {mid} index')






