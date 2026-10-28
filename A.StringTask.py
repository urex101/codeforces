#118A


word = input().lower()

vowels = ['a', 'o', 'y', 'e', 'u', 'i']
result = ""
for i in word:
    if i not in vowels:
        result += "." + i
    else:
        continue

print(result)