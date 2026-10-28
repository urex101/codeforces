#1A
import math

n,m,a = map(int,input().split())

flags_needed = 0

columns = math.ceil(n / a)
rows = math.ceil(m / a)
flags_needed = columns * rows
print(flags_needed)