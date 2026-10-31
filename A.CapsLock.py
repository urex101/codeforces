#131A

word = input("")
word_casechange = word.swapcase()
if word[1:].isupper():
    print(word_casechange)
elif len(word) == 1:
    print(word_casechange)
else:
    print(word)
