matrix_row1 = input("").strip(" ")
matrix_row2 = input("").strip(" ")
matrix_row3 = input("").strip(" ")
matrix_row4 = input("").strip(" ")
matrix_row5 = input("").strip(" ")


matrix = [matrix_row1, matrix_row2, matrix_row3, matrix_row4, matrix_row5]

for row in matrix:
    if "1" in row:
        row_index = matrix.index(row)
        column_index_wrong = row.index("1")
        column_index = int(column_index_wrong)  
        fix_column_index = column_index / 2

        break
#remove the 0.x value from the column index and make it an integer
fix_column_index = int(fix_column_index)
print(abs(row_index - 2) + abs(fix_column_index - 2))