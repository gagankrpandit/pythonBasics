# Python program to find the Nth term in a Fibonacci series

num = int(input('Enter Nth term: '))
list_ = [0, 1, 1]

i = 2
j = 0
k = 1
while i < num:
    list_[i] = list_[j] + list_[k]
    list_.append(i)
    i = i + 1
    j = j + 1
    k = k + 1

list_ = list_[:-1]
print(list_[num-1])
