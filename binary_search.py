# Python program to implement binary search

aList = [54, 67, 85, 33, 92, 74, 75, 35, 66, 32, 24]
aList.sort()
print(f'Given list is: {aList}')

low = 0
upp = len(aList) - 1
mid = (low + upp) // 2

num = int(input(f'Enter number from list: '))

while num != aList[mid]:
    mid = (low + upp) // 2
    if num > aList[mid]:
        low = mid + 1
    else:
        upp = mid - 1
print(f'found at {mid} index position')
