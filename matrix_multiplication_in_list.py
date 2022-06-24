# Python program to implement matrix multiplication

m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[1,2,3], [4,5,6], [7,8,9]]
m3 = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j] = m1[i][j] * m2[i][j]
for k in range(len(m3)):
    print(m3[k])
