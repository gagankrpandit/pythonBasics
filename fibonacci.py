# Python program to find the Nth term in a Fibonacci series

num = int(input('Enter Nth term: '))
list_ = [1, 2, 3]

i = 2
j = 0
k = 1
while i < num:
    list_[i] = list_[j] + list_[k]
    list_.append(i)
    i = i + 1
    j = j + 1
    k = k + 1
print(list_[:-1])

