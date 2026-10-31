#339B

numberofhouses , tasks = map(int, input().split())
houses_task = list(map(int, input().split()))
t = 0
current_house = 1
for i in range(tasks):
    if houses_task[i] >= current_house:
        t += houses_task[i] - current_house
        current_house = houses_task[i]
    else:
        t += numberofhouses - current_house + houses_task[i]
        current_house = houses_task[i]

print(t)