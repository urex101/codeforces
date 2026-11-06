#Round196 Problem B
import sys
input = sys.stdin.read
data = list(map(int, input().split()))
numberoftests = int(data[0])
answers = []
index = 1
for i in range(numberoftests):
    testcase = int(data[index])
    index += 1
    stringofnums = data[index:index+testcase]
    index += testcase
    answer = testcase
    for i in set(stringofnums):
        eliminated = 0
        for x in stringofnums:
            if x % i != 0:
                eliminated += 1

        if eliminated < answer:
            answer = eliminated
    answers.append(answer)
for answer in answers:
    print(answer)