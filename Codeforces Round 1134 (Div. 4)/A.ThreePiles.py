answers = []
numberoftestcases = int(input())
for _ in range(numberoftestcases):
    a, b, c = map(int, input().split())
    lowest = min(a, b, c)
    highest = max(a, b, c)
    middle = a + b + c - lowest - highest
    if a == b or b == c or a == c:
        answers.append("NO")
    elif highest - middle == 1 and middle - lowest == 1:
        answers.append("YES")
    else:
        answers.append("NO")
for answer in answers:
    print(answer)
