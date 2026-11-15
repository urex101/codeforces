#734A
import sys
input = sys.stdin.readline
Gamecount = int(input())
games = input().strip()
anton = 0
danik = 0
for i in range(Gamecount):
    if games[i] == "A":
        anton += 1
    elif games[i] == "D":
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")