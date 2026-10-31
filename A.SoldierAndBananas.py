#546A
k,n,w = input().split(" ")
cost = 0
for i in range(int(w)):
    cost += int(k) * (i + 1)

borrowed = cost - int(n)
if borrowed <= 0:
    print(0)
else:
    print(abs(borrowed))