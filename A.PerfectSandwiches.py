#2276A
numberofcases = int(input())
answers = []
for _ in range(numberofcases):
    cheese, sasuge = map(int, input().split())
    if sasuge >= cheese:
        answers.append(-1)
    else:
        answers.append(min(sasuge, cheese - sasuge))


for answer in answers:
    print(answer)