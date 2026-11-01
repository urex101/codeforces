#1374C

numberofenteries = int(input())
for i in range(numberofenteries):
    bracketnum = int(input())
    bracketstring = input()
    brackettest = 0
    moves = 0
    for bracket in bracketstring:
        if bracket == '(':
            brackettest += 1
        elif bracket == ')':
            brackettest -= 1
        if brackettest < 0:
            moves += 1
            brackettest = 0
    print(moves)