
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
print("Enter the elements of magic square:")
for i in range(0,3):
    matrix.append([])
    for j in range(0,3):
        element = input()
        matrix[i].append(element)
print("Matrix is:")
print matrix
magic_check(matrix)
