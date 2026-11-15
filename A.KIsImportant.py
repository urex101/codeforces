#2268A
import sys
index = 0
input = sys.stdin.readline
number_of_tests = int(input())
scores = []
for _ in range(number_of_tests):
    listlength , param = map(int, input().split())
    numbers = list(map(int, input().split()))
    score = 0
    while len(numbers) >= param:
        lenfy = param - 1 
        righty= len(numbers) - param
        if numbers[lenfy] > numbers[righty]:
            score += numbers[lenfy]
            numbers.pop(lenfy)
        else:
            score += numbers[righty]
            numbers.pop(righty)
    scores.append(score)

for score in scores:
    print(score)