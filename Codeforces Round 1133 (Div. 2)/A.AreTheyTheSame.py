#A. Are They the Same?
answers = []
testcases = int(input())
for i in range(testcases):
    lentgh , k = map(int, input().split())
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    array1.sort()
    
    array2.sort()
    if k % 2 == 0:
        evens_a = 0
        for i in array1:
            if i % 2 == 0:
                evens_a = evens_a + 1
        evens_b = 0
        for i in array2:
            if i % 2 == 0:
                evens_b = evens_b + 1
        if evens_a <= evens_b:
            answers.append("YES")
        else:
            answers.append("NO")
    elif k % 2 == 1:
        evens_a = 0
        for i in array1:
            if i % 2 == 0:
                evens_a = evens_a + 1
        evens_b = 0
        for i in array2:
            if i % 2 == 0:
                evens_b = evens_b + 1
        answers.append("YES" if evens_a >= evens_b else "NO")
    else:
        if sorted(array1) == sorted(array2):
            answers.append("YES")
        else:
            answers.append("NO")

for answer in answers:
    print(answer)