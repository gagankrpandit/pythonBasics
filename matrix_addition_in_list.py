# Python program to implement matrix addition

mat = [[1,2,3], [4,5,6], [7,8,9]]
cat = [[1,2,3], [4,5,6], [7,8,9]]
xat = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(mat)):
    for j in range(len(mat[i])):
        xat[i][j] = mat[i][j] + cat[i][j]
for k in xat:
    print(k)
