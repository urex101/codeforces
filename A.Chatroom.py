#58A
import re
text = input("")


def checkforhello(x):
    return bool(re.search(r'h.*e.*l.*l.*o', x))

if checkforhello(text):
    print("YES")
else:
    print("NO")