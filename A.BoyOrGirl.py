#236A

name = input("")

carachters_in_name = []

for i in name:
    if i not in carachters_in_name:
        carachters_in_name.append(i)


if len(carachters_in_name) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")