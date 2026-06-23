matrix =[[10,20,30],[40,50,60],[70,80,90]]
a=[row[i] for row in matrix for i in range(len(matrix[0]))]

print("Transpose of matrix is:",a)
for row in matrix:print(row)


