numberoftestcases = int(input())
answers = []
for _ in range(numberoftestcases):
    lengthofstring = int(input())
    string = input()
    answer = int(0)
    nextcol = "R"
    for i in range(lengthofstring):
        if string[i] == nextcol:
            if nextcol == "R":
                nextcol = "B"
            else:
                nextcol = "R"
        else:
            answer += 1
    answers.append(answer)

for answer in answers:
    print(answer)