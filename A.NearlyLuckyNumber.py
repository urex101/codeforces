#110A
import sys

number = sys.stdin.readline().strip()
luckycount = 0
for digit in number:
    if digit == "4" or digit == "7":
        luckycount += 1

if luckycount == 4 or luckycount == 7:
    print("YES")
else:
    print("NO")