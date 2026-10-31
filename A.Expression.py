#479A

a = input()
b = input()
c = input()
a = int(a)
b = int(b)
c = int(c)

if a == 1 and b > 1 and c > 1:
    print((a+b)* c)
elif b == 1 and a > c:
    print(a*(b+c))
elif b == 1 and c > a:
    print((b+a)*c)
elif c== 1 and a > 1 and b > 1:
    print(a*(b+c))
elif a == 1 and b == 1 and c == 1:
    print(a+b+c)
elif a == 1 and b == 1 and c > 1:
    print((a+b)*c)
elif a == 1 and c == 1 and b > 1:
    print(a+b+c)
elif b == 1 and c == 1 and a > 1:
    print((b+c)*a)
elif b== 1 and a> 1 and c > 1:
    print((a+b)*c)
else:
    print(a*b*c)