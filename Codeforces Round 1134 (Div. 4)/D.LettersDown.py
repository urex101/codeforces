import sys

data = sys.stdin.read().splitlines()
index = 0
numberoftests = int(data[index])
index += 1
answers = []
for _ in range(numberoftests):
    stringlength = int(data[index])
    index += 1
    string = data[index]
    index += 1
    alphabetindex = dict(
        a=1,
        b=2,
        c=3,
        d=4,
        e=5,
        f=6,
        g=7,
        h=8,
        i=9,
        j=10,
        k=11,
        l=12,
        m=13,
        n=14,
        o=15,
        p=16,
        q=17,
        r=18,
        s=19,
        t=20,
        u=21,
        v=22,
        w=23,
        x=24,
        y=25,
        z=26,
    )
    values = []
    for letter in string:
        values.append(alphabetindex[letter])

    resets = 0

    while True:
        missmatch = []
        for i in range(stringlength // 2):
            if values[i] != values[stringlength - 1 - i]:
                missmatch.append((values[i]))
                missmatch.append((values[stringlength - 1 - i]))
        if len(missmatch) == 0:
            break
        biggest = max(missmatch)
        for i in range(stringlength):
            if values[i] == biggest:
                values[i] -= 1
        resets += 1
    answers.append(str(resets))
for answer in answers:
    print(answer)
