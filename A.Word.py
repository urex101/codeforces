#59A

word = input("")
uppercase_count = 0
lowercase_count = 0
for i in range(len(word)):
    if word[i].isupper():
        uppercase_count += 1
    else:
        lowercase_count += 1

if uppercase_count > lowercase_count:
    print(word.upper())
else:
    print(word.lower())