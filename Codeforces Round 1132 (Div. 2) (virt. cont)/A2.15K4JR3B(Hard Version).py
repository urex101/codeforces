#A.15K4JR3B (Hard Version)


operationcount = int(input())
areas = []
for i in range(operationcount):
    area = 0
    number = int(input())
    sequence = list(map(int, input().split()))
    sequence.sort(reverse=True)
    base = 0
    height = 0
    for i in sequence:
        if base <= height:
            base += 2**i
        else:
            height += 2**i
    areas.append(base * height)

for area in areas:
    print(area)