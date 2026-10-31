#339A

equasion = input().split('+')

equasion = [int(x) for x in equasion]
equasion.sort()
print('+'.join(str(x) for x in equasion))