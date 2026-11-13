#977A

number, subtractions = map(int, input().split())
number = str(number)
for _ in range(subtractions):
    if number[-1] != '0':
        number = str(int(number) - 1)
    else:
        number = str(int(number) // 10)

print(number)