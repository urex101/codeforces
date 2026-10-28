#69A


rows = input()
matrix = []

for i in range(int(rows)):
    x, y, z = input().split(" ")
    matrix.append((x, y, z))




sumallx = 0
sumally = 0
sumallz = 0

for j in range(len(matrix)):
    sumallx += int(matrix[j][0])
    sumally += int(matrix[j][1])
    sumallz += int(matrix[j][2])
if sumallx == 0 and sumally == 0 and sumallz == 0:
    print("YES")
else:
    print("NO")