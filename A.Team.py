question_count = int(input(""))

x = int(0)
for i in range(question_count):
    certain = input("")
    a,b,c = certain.split( )
    if int(a) + int(b) + int(c) >= 2:
        x += 1
print(x)