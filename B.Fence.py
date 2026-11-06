#363B
import sys
input = sys.stdin.read

data = input().split()
planks = int(data[0])
width = int(data[1])
planks_list = [int(x) for x in data[2:planks + 2]]
current = sum(planks_list[:width])
minimum = current
index = 0
for i in range(planks - width):
    current = current - planks_list[i] + planks_list[i + width]
    if current < minimum:
        minimum = current
        index = i + 1
print(index + 1)
