#41A

wordone = input("")
wordtwo = input("")

if len(wordone) != len(wordtwo):
    print("NO")
elif wordone[::-1] == wordtwo:
    print("YES")
else:
    print("NO")