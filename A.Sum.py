#1742A
numberof_test_cases = int(input())
answers = []
for i in range(numberof_test_cases):
    num1 , num2, num3 = map(int, input().split())
    if num1 + num2 == num3:
        answers.append("YES")
    elif num1 + num3 == num2:
        answers.append("YES")
    elif num2 + num3 == num1:
        answers.append("YES")
    else:
        answers.append("NO")

for answer in answers:
    print(answer)