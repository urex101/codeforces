import sys

data = sys.stdin.read().splitlines()
index = 0
numberofgames = int(data[index])
answers = []
for _ in range(numberofgames):
    numberofpiles, rockpremise = map(int, data[index + 1].split())
    piles = list(map(int, data[index + 2].split()))
    index += 2
    x = 0
    total = 0
    while x < numberofpiles:
        total += piles[x]
        x += rockpremise + 1

    if total % 2 == 1:
        answers.append("Alice")
    else:
        answers.append("Bob")

sys.stdout.write("\n".join(answers) + "\n")