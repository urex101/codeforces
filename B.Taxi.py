#158B

groupnumber = int(input())
groups = input()
nums = [int(x) for x in groups.split()]

ones = nums.count(1)
twos = nums.count(2)
threes = nums.count(3)
fours = nums.count(4)

taxis = 0

taxis = fours         
while threes > 0:
    taxis += 1
    threes -= 1
    if ones > 0:
        ones -= 1               
while twos >= 2:
    taxis += 1
    twos -= 2
if twos == 1:
    taxis += 1
    if ones >= 2:
        ones -= 2
    else:
        ones = 0   
while ones >= 4:
    taxis += 1
    ones -= 4
if ones > 0:
    taxis += 1

print(taxis)