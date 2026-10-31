operation_count = int(input(""))

x = int(0)
for i in range(operation_count):
    operation = input("")
    if operation == "++X" or operation == "X++":
        x += 1
    elif operation == "--X" or operation == "X--":
        x -= 1

print(x)