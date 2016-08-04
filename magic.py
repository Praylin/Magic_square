import random

#Function checks whether the given matrix is a magic square
def magic_check(matrix):
    #Extract column
    for j in range(0,3):
        sli = [matrix[i][j] for i in range(0,3)]
        colum_sum.append(sum(sli))
    #Extract rows
    for row in matrix:
        row_sum.append(sum(row))

    row_check = all(x==colum_sum[0] for x in colum_sum)
    column_check = all(x==row_sum[0] for x in row_sum)
    if (row_check == True and column_check == True):
        print("This is a Magic Square.")
    else:
        print("Not a Magic Square.")

# Enter the magic_square elements
matrix = []
colum_sum = []
row_sum = []
for i in range(0,3):
    matrix.append(random.sample(range(1, 9), 3))

# s1 = set(matrix[0])
# s2 = set(matrix[1])
# s3 = set(matrix[2])
# print s1.intersection(s2)
# print s2.intersection(s3)
# print s3.intersection(s1)
print("Matrix is:")
print matrix

magic_check(matrix)
