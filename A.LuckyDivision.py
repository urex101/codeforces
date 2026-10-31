#122A

number = int(input())
def checkforlucky(num):
    x = 0
    for digit in str(num):
    
        if digit == "4" or digit == "7":
            x += 1
    if x == len(str(num)):
        return True
    else:
        return False
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
for lucky in lucky_numbers:
    if number % lucky == 0:
        print("YES")
        break
else:
    if checkforlucky(number):
        print("YES")
    else:
        print("NO")
