#2278A
numberof_test_cases = int(input())
answers = []
for _ in range(numberof_test_cases):
    wordonelen, wordtwolen = map(int, input().split())
    wordone = list(input())
    wordtwo = list(input())
    elliminateall = True
    for letter in wordtwo:
        if wordtwo.count(letter) > wordone.count(letter):
            elliminateall = False
    leftoverissix = True
    if len(wordone) - len(wordtwo) != 3:
        leftoverissix = False
    for letter in "six":
        if wordone.count(letter) - wordtwo.count(letter) != 1:
            leftoverissix = False

    if elliminateall and leftoverissix:
        answers.append("YES")
    else:
        answers.append("NO")
for answwer in answers:
    print(answwer)
