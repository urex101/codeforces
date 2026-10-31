#43A

description_lines = int(input())
description = dict()
#the discription contains the scorer of the goal, just their name, our goal here is to find the winner of the game
for i in range(description_lines):
    scorer = input()
    if scorer in description:
        description[scorer] += 1
    else:
        description[scorer] = 1

print(max(description, key=description.get))