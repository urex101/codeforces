import sys
data = sys.stdin.read().splitlines()
index = 0 
testcases = int(data[index])
index += 1
answers = []
for _ in range(testcases):
    length = int(data[index])
    index += 1
    string = list(map(int, data[index].split()))
    index += 1
    seencount = int(0)
    stringorder = sorted(string)
    if True:
        lefthand = []
        righthand = []
        for i in range(len(stringorder)):
            if i % 2 == 0:                      
                lefthand.append(stringorder[i])
            else:                                
                righthand.append(stringorder[i])
    righthand.reverse()
    stringfix = lefthand + righthand
    seencount += len(set(lefthand)) + len(set(righthand))
    string = " ".join(map(str, stringfix))



    answers.append(str(seencount))
    answers.append(string)

sys.stdout.write("\n".join(answers) + "\n")