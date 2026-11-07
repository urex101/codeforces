#B. Introduction to the Niche Internet
number_of_test_cases = int(input())
answers = []
for _ in range(number_of_test_cases):
    numberofdonos , pleasentdonosneeded = map(int, input().split())
    donos = list(map(int, input().split()))
    donos.sort()
    unpleasantdonos = numberofdonos - pleasentdonosneeded
    fixedsequence = []
    average = 0

    if unpleasantdonos == 0 :
        fixedsequence = donos[unpleasantdonos:] + donos[:unpleasantdonos][::-1]
        answers.append("YES")
        answers.append(" ".join(map(str, fixedsequence)))
    elif donos[unpleasantdonos - 1] < donos[-1]:
        fixedsequence = donos[unpleasantdonos:] + donos[:unpleasantdonos][::-1]
        answers.append("YES")
        answers.append(" ".join(map(str, fixedsequence)))
    else:
        answers.append("NO")

    
for answer in answers:
    print(answer)