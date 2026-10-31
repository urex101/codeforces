#791A

bothweights = input().split()

limak, bob = bothweights
limak = int(limak)
bob = int(bob)
count = 0

while limak <= bob:
    limak *= 3
    bob *= 2
    count += 1

print(count)