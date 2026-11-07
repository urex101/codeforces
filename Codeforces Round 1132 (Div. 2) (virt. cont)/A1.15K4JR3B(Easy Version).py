#A.15K4JR3B (Easy Version)
import sys

data = sys.stdin.read().split()
numberofoperations = int(data[0])
operations = list(map(int, data[1:]))
areas = []
for operation in range(len(operations)):
    height = 0
    base = 0
    if operations[operation] % 2 == 0:
        height = int(operations[operation]) // 2
        base = int(operations[operation]) // 2
        area = height * base
        areas.append(area)
    else:
        height = int(operations[operation]) // 2
        base = int(operations[operation]) // 2 + 1
        area = height * base
        areas.append(area)

for area in areas:
    print(area)
