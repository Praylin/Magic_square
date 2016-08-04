
# Enter the magic_square elements

matrix = []
size = raw_input("Enter the number of rows & cols:")
for i in range(0,int(size)):
    matrix.append([])
    for j in range(0,int(size)):
        element = input()
        matrix[i].append(element)

print matrix;
