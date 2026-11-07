#Round196 Problem A

testcases = int(input())
answers = []
for i in range(testcases):
    first, second = map(int, input().split())
    if first == second:
        answers.append(0)
    elif abs(first) == abs(second):
        answers.append(0)
    elif first == 0 and second > 0:
        answers.append(second-1)
    elif first < 0 and second == 0:
        answers.append(abs(first)-1)    
    elif first > 0 and second > 0:
        answers.append(second - first)
    elif first < 0 and second < 0:
        answers.append(abs(first) - abs(second))
    elif first < 0 and second > 0:
        if abs(first) > second:
            x = (abs(first) - abs(second))
            if x == 1:
                answers.append(0)
            else:
                answers.append(x-1)
        elif abs(first) < second:
            x = (abs(second) - abs(first))
            if x == 1:
                answers.append(0)
            else:
                answers.append(x-1)
for i in range(len(answers)):
    print(answers[i])