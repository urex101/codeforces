#112A


abcd_vallued = {    "a": 1,    "b": 2,    "c": 3,    "d": 4,    "e": 5,    "f": 6,    "g": 7,    "h": 8,    "i": 9,    "j": 10,   "k": 11,    "l": 12,    "m": 13,    "n": 14,    "o": 15,    "p": 16,    "q": 17,    "r": 18,    "s": 19,    "t": 20,    "u": 21,    "v": 22,    "w": 23,    "x": 24,    "y": 25,    "z": 26}


input_string1 = input("").lower()
input_string2 = input("").lower()

string1_value = 0
string2_value = 0

x = len(input_string1)

for i in range(x):
    string1_value += abcd_vallued[input_string1[i]]
    string2_value += abcd_vallued[input_string2[i]]
    if string1_value > string2_value:
        print("1")
        break
    elif string1_value < string2_value:
        print("-1")
        break
    else:
        continue

if string1_value == string2_value:
    print("0")